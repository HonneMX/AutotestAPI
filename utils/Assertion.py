import json
from json.decoder import JSONDecodeError

import allure
from requests import Response

"""Метеды для проверки поступающих запросов"""


class Assertions():

    @staticmethod
    def check_status_code(response: Response, status_code):
        """Метод проверяет поступающий код ответа сервера"""
        with allure.step(
                f"Сравниваем текущий код ответа сервера {response.status_code} и ожидаемый код ответа сервера {status_code}"):
            assert status_code == response.status_code
            if response.status_code == status_code:
                with allure.step(f"Success! Код ответа сервера: {response.status_code}"):
                    pass
            elif response.status_code == 404:
                with allure.step(f"Книга не существует или была удалена. Код ответа сервера: {response.status_code}"):
                    pass
            else:
                raise Exception(f"Error! Код ответа сервера: {response.status_code}")

    @staticmethod
    def check_requerment_fields(response: Response, expected_value):
        """Метод для проверки наличия обязательных полей в ответе запроса"""
        with allure.step(f"Проверяем в ответе наличие всех полей {expected_value}"):
            try:
                token = json.loads(response.text)
                with allure.step(f"Сравниваем поля {list(token)} и ожидаемые: {expected_value}"):
                    assert list(token) == expected_value
            except:
                with allure.step(f"Ошибка сравнения списка полей {list(token)} и ожидаемых: {expected_value}"):
                    raise Exception(f"Something wrong assert keys of json")

    @staticmethod
    def check_value_requerment_fields(response: Response, filed_name, expected_value):
        """Метод для проверки наличия обязательных полей в ответе запроса"""
        with allure.step(f"Ожидаемое значение: {expected_value} фактическое: {filed_name}"):
            try:
                check = response.json()
                check_info = check.get(filed_name)
                assert  check_info == expected_value
            except JSONDecodeError:
                print(f"Response is not JSON format")