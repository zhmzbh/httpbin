# API自动化测试项目

## 项目简介
这是一个使用Python + Pytest + Requests编写的API自动化测试项目。

## 技术栈
- Python 3.13
- Pytest 9.0.3
- Requests库
- Faker测试数据生成

## 如何运行

# 安装依赖
pip install pytest requests faker

# 运行测试
pytest -v -s

#项目结构
├── config/          # 配置文件
├── testcases/       # 测试用例
├── utils/           # 工具函数
└── conftest.py      # pytest配置

#测试覆盖
POST请求测试
GET请求测试
异常数据处理测试
