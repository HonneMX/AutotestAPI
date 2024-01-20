import json

import allure

from enviroment import ENV_ONJECT
from utils.Assertion import Assertions
from utils.http_methods import Http_methods

"""Методы для тестирования API"""

base_url = ENV_ONJECT.get_base_url()


class ApiResfullBooker():

    """Метод получения токена аутентификации"""

    @staticmethod
    def auth_user(user, password):
        auth_uri = '/auth'
        payload = {
            "username": user,
            "password": password
        }
        jsoned_payload = json.dumps(payload,indent=3)
        with allure.step(f"Get auth token for user: {user} and password: {password}"):
            try:
                response_json = Http_methods.post(base_url+auth_uri,jsoned_payload)
                Assertions.check_status_code(response_json,200)
            except:
                raise Exception(f"Something wrong. Auth token: {response_json.json()['token']}")
            return response_json

    """Метод для получения списка книг"""

    @staticmethod
    def get_list_of_books():
        get_books_uri='/booking'
        with allure.step(f"Get list of books"):
            try:
                book_list = Http_methods.get(base_url+get_books_uri)
                Assertions.check_status_code(book_list, 200)
            except:
                raise Exception(f"Something wrong with books: {book_list}")
            return book_list

    """Метод для получения данных по конкретной книге"""
    @staticmethod
    def get_book_by_id(book_id):
        get_books_uri = f'/booking/{book_id}'
        with allure.step(f"Get book by id: {book_id}"):
            book_list = Http_methods.get(base_url+get_books_uri)
            Assertions.check_status_code(book_list, 200)

            return book_list

    @staticmethod
    def create_generated_book(book_payload):
        books_uri = '/booking'
        with allure.step(f"Creating book with data: {book_payload}"):
            try:
                response_book_create = Http_methods.post(base_url+books_uri,book_payload)
                Assertions.check_status_code(response_book_create, 200)
            except:
                raise Exception(f"Something wrong with creating book")
            return response_book_create

    @staticmethod
    def update_generated_book(book_id,data,token):
        books_update_uri = f'/booking/{book_id}'

        with allure.step(f"Update book with id: {book_id} with data: {data}"):
            try:
                Http_methods.headers.update({'Cookie':f'token={token}'})
                response_book_update = Http_methods.put(base_url+books_update_uri,data)
                Assertions.check_status_code(response_book_update, 200)
            except:
                raise Exception(f"Something wrong with creating book")
            return response_book_update

    @staticmethod
    def delete_generated_book(book_id,token):
        books_delete_uri = f'/booking/{book_id}'

        with allure.step(f"Delete book with id: {book_id} "):
            Http_methods.headers.update({'Cookie': f'token={token}'})
            response_book_delete = Http_methods.delete(base_url+books_delete_uri)
            return response_book_delete

