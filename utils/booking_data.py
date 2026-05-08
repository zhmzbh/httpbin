from faker import Faker
import random

fake = Faker('zh_CN')

def generate_valid_booking_data():
    """生成有效的预约数据"""
    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": random.randint(50, 2000),
        "depositpaid": random.choice([True, False]),
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-01-10"
        },
        "additionalneeds": random.choice(["Breakfast", "Parking", "Late checkout", None])
    }

def generate_update_data():
    """生成更新数据"""
    return {
        "firstname": fake.first_name(),
        "totalprice": random.randint(100, 500)
    }