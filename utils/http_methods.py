import allure
import requests
from utils.Logger import Logger
from enviroment import ENV_ONJECT

"""Список HTTP методов"""


class Http_methods:
    headers = {'Content-Type': 'application/json','Accept':'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("Request method GET"):
            Logger.add_request(url, method_name='GET')
            try:
                result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
            except:
                result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie, verify=False)
                Logger.add_response_verify()
            Logger.add_response(result)
            return result

    @staticmethod
    def post(url, body):
        with allure.step("Request method POST"):
            Logger.add_request(url, method_name='POST')
            Logger.add_request_data(body)
            Logger.add_request_headers(Http_methods.headers)
            try:
                result = requests.post(url, data=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            except:
                result = requests.post(url, data=body, headers=Http_methods.headers, cookies=Http_methods.cookie,
                                       verify=False)
                Logger.add_response_verify()
            Logger.add_response(result)
            return result

    @staticmethod
    def delete(url):
        with allure.step("Request method DELETE"):
            Logger.add_request(url, method_name='DELETE')
            Logger.add_request_headers(Http_methods.headers)
            try:
                result = requests.delete(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
            except:
                result = requests.post(url,  headers=Http_methods.headers, cookies=Http_methods.cookie,
                                       verify=False)
                Logger.add_response_verify()
            Logger.add_response(result)
            return result

    @staticmethod
    def put(url, body):
        with allure.step("Request method PUT"):
            Logger.add_request(url, method_name='PUT')
            Logger.add_request_data(body)
            Logger.add_request_headers(Http_methods.headers)
            try:
                result = requests.put(url, data=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            except:
                result = requests.post(url, data=body, headers=Http_methods.headers, cookies=Http_methods.cookie,
                                       verify=False)
                Logger.add_response_verify()
            Logger.add_response(result)
            return result

    @staticmethod
    def set_headers(data):
        """Метод добавляющий в headers дополнительные заголовки"""
        with allure.step("Добавлям новые данные в headers"):
            try:
                Http_methods.headers.update(data)
            except:
                print("Can't add new data to headers")

    @staticmethod
    def get_content_length(content):
        try:
            header = {"Content-Length": str(len(content))}
            return header
        except:
            print("Something goes wrong with Content-Length")
