import requests
from utils.config import BASE_URL
from utils.api_helpers import post
from utils.logger import get_logger

logger = get_logger(__name__)

def test_login_user(register_user):
    logger.info(f"Login test started for email: {register_user['email']}")
    response = post("/auth/login", json=register_user)
    logger.info(f"Response status: {response.status_code}, body: {response.text}")
    assert response.status_code == 200, "Login failed"
    data = response.json()
    assert "token" in data, "Token not found in response"
    assert "user" in data, "User data missing in response"
    assert data["user"]["email"] == register_user["email"]
    logger.info("Login test passed")