import allure
import pytest

from utils.Assertion import Assertions
from utils.Generators import GeneratedBook
from utils.api import ApiResfullBooker
from utils.http_methods import Http_methods


@allure.epic("Test check CRUD items")
@allure.tag("API", "CRUD")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "IaushevSV")
class TestCRUDBooker():


    @allure.title("Test get all books from library")
    @allure.description("Проверяем получение всего списка книг")
    def test_get_books_list(self):
        response = ApiResfullBooker.get_list_of_books()
        Assertions.check_requerment_fields(response,['bookingid'])

    book_list=[
        (908),
        (907),
        (906)
    ]
    @allure.title("Test get certain book from library. Get by id")
    @allure.description("Проверяем получение конкретной книги по идентификатору")
    @pytest.mark.parametrize('book_id',book_list)
    def test_get_books_list_bu_id(self,book_id):
        book_response = ApiResfullBooker.get_book_by_id(book_id)
        Assertions.check_requerment_fields(book_response, ["firstname","lastname","totalprice","depositpaid","bookingdates","additionalneeds"])

    @allure.title("Test create fake book")
    @allure.description("Проверяем создание книги")
    def test_create_fake_book(self):
        new_book = GeneratedBook()
        json_for_book_create= new_book.get_fake_book()
        Http_methods.headers.update(Http_methods.get_content_length(json_for_book_create))
        response_book =ApiResfullBooker.create_generated_book(json_for_book_create)
        with allure.step(f"Создана книга с id:{response_book.json()['bookingid']}"):
            pass


    @allure.title("Test update book")
    @allure.description("Тест проверяет изменение книги")
    def test_update_fake_book(self):
        new_book = GeneratedBook()
        response_auth_json = ApiResfullBooker.auth_user('admin','password123')
        json_for_book_create = new_book.get_fake_book()
        response_created_book = ApiResfullBooker.create_generated_book(json_for_book_create)
        new_book.id = response_created_book.json()['bookingid']
        new_book.depositpaid = 1000
        updated_book_response = ApiResfullBooker.update_generated_book(new_book.id,new_book.get_fake_book(),response_auth_json.json()['token'])
        Assertions.check_status_code(updated_book_response,200)


    @allure.title("Test delete book")
    @allure.description("Тест проверяет удаление созданной книги")
    def test_delete_fake_book(self):
        new_book = GeneratedBook()
        response_auth_json = ApiResfullBooker.auth_user('admin', 'password123')
        json_for_book_create = new_book.get_fake_book()
        response_created_book = ApiResfullBooker.create_generated_book(json_for_book_create)
        new_book.id = response_created_book.json()['bookingid']
        ApiResfullBooker.delete_generated_book(new_book.id,response_auth_json.json()['token'])
