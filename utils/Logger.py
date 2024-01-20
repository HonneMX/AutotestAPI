import datetime
import os

from requests import Response

"""Методы покрывающие логированием остальные методы"""


class Logger():
    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, method_name: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name} \n"
        data_to_add += f"Request url: {url} \n"
        data_to_add += f"Time: {str(datetime.datetime.now())} \n"
        data_to_add += f"Request method: {method_name} \n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, result: Response):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        data_to_add = f"Response code: {result.status_code} \n"
        data_to_add += f"Response text: {result.text} \n"
        data_to_add += f"Response headers: {headers_as_dict} \n"
        data_to_add += f"Response cookies: {cookies_as_dict} \n"
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_response_verify(cls):
        data_to_add = f"Certificate verify failed. Connect to 80 port \n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_request_data(cls, data: str):
        data_to_add = f"Body_data: {data} \n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_request_headers(cls, headers: dict):
        data_to_add = f"Request headers: {headers} \n"
        cls.write_log_to_file(data_to_add)
