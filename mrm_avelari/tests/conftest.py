import pytest
from faker import Faker
from utils.config import BASE_URL
from utils.api_helpers import post
from utils.logger import get_logger

fake = Faker("ru_RU")

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logger = get_logger("global")
    logger.info("=== Starting test session ===")
    yield
    logger.info("=== Finishing test session ===")

@pytest.fixture
def user_credentials():
    return {
        "email": fake.unique.email(),
        "password": fake.password(length=8),
        "age": fake.random_int(min=0, max=99)
    }

@pytest.fixture
def register_user(user_credentials):
    response = post("/auth/register", json=user_credentials)
    assert response.status_code in [200, 422], "User registration failed"
    return user_credentials

@pytest.fixture
def auth_token(register_user):
    response = post("/auth/login", json=register_user)
    assert response.status_code == 200, "Login failed"
    return response.json()["token"]

@pytest.fixture
def new_user_name():
    return fake.first_name()

@pytest.fixture
def not_exist_email():
    return fake.unique.email()