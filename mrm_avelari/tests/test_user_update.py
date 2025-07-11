from utils.config import BASE_URL
from utils.api_helpers import patch
from utils.logger import get_logger

logger = get_logger(__name__)

def test_update_user_name(auth_token, new_user_name):
    logger.info(f"Updating user name to: {new_user_name}")
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"name": new_user_name}

    response = patch("/user/name", json=payload, headers=headers)
    logger.info(f"Update response status: {response.status_code}")
    assert response.status_code == 200, "Failed to update user name"
    data = response.json()
    assert "user" in data, "User data missing in response"
    assert data["user"]["name"] == new_user_name, "Name update failed"
    logger.info("User name updated successfully")