import allure
import pytest

from utils.Assertion import Assertions
from utils.api import ApiResfullBooker


@allure.epic("Test check auth for users")
@allure.tag("API", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "IaushevSV")
class TestAuthentification():

    user_list = [
        ('admin', 'password123'),
        ('admin', ' '),
        (' ', 'password123'),
        (' ', ' ')


    ]

    @allure.title("Test user authentication")
    @allure.description("Проверка успешной аутентификации пользователя")
    @pytest.mark.parametrize('username,password', user_list)
    def test_auth_users(self,username,password):
        token = ApiResfullBooker.auth_user(username,password)
        Assertions.check_requerment_fields(token, ['token'])


