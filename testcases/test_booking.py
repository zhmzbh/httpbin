import pytest
import requests
from config.config import BASE_URL, ENDPOINTS
from utils.booking_data import generate_valid_booking_data

class TestBookingAPI:

    def setup_method(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        print("\n[Setup] 测试开始")

    def teardown_method(self):
        self.session.close()
        print("[Teardown] 测试结束\n")

    def test_01_post_request(self):
        """测试POST请求"""
        test_data = generate_valid_booking_data()
        print(f"发送数据: {test_data}")

        url = f"{self.base_url}{ENDPOINTS['create_booking']}"
        response = self.session.post(url, json=test_data)

        print(f"状态码: {response.status_code}")

        assert response.status_code == 200
        response_json = response.json()
        # httpbin会将发送的数据原样返回
        assert response_json["json"] == test_data
        print("POST请求测试通过！")

    def test_02_get_request(self):
        """测试GET请求"""
        url = f"{self.base_url}{ENDPOINTS['get_booking']}"
        params = {"name": "张三", "id": 123}

        response = self.session.get(url, params=params)

        assert response.status_code == 200
        response_json = response.json()
        # 验证参数被正确接收
        assert response_json["args"]["name"] == "张三"
        assert response_json["args"]["id"] == "123"
        print("GET请求测试通过！")

    def test_03_invalid_data(self):
        """测试无效数据（发送错误的内容类型）"""
        url = f"{self.base_url}{ENDPOINTS['create_booking']}"
        # 发送一个错误的请求（比如发送纯文本而不是JSON）
        response = self.session.post(url, data="这不是JSON")

        print(f"状态码: {response.status_code}")
        # httpbin还是会返回200，但我们可以检查响应
        # 实际项目中无效数据应该返回400，这里只是演示
        assert response.status_code == 200
        print("测试完成")

    def test_04_put_request(self):
        """测试PUT请求"""
        url = f"{self.base_url}{ENDPOINTS['update_booking']}"
        test_data = {"id": 1, "name": "更新后的数据"}

        response = self.session.put(url, json=test_data)

        assert response.status_code == 200
        response_json = response.json()
        assert response_json["json"] == test_data
        print("PUT请求测试通过！")

    def test_05_delete_request(self):
        """测试DELETE请求"""
        url = f"{self.base_url}{ENDPOINTS['delete_booking']}"

        response = self.session.delete(url)

        assert response.status_code == 200
        print("DELETE请求测试通过！")

    class TestParameterized:
        """参数化测试示例"""

    @pytest.mark.parametrize("name,age,expected", [
        ("张三", 18, "成人"),
        ("李四", 6, "儿童"),
        ("王五", 65, "老人"),
        ("", 20, "姓名不能为空"),
    ])
    def test_user_info(self, name, age, expected):
        """参数化测试：用同一段代码测试多组数据"""
        print(f"\n测试数据: name={name}, age={age}, 期望={expected}")

        url = f"{BASE_URL}/post"
        data = {"name": name, "age": age}
        response = requests.post(url, json=data)

        assert response.status_code == 200

        # 这里是模拟的业务逻辑判断
        if len(name) == 0:
            result = "姓名不能为空"
        elif age < 18:
            result = "儿童"
        elif age >= 60:
            result = "老人"
        else:
            result = "成人"

        assert result == expected
        print(f"实际结果: {result} ")