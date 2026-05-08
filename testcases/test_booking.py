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





