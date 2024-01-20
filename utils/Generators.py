import json

from faker import Faker

fake = Faker()

class GeneratedBook():
    """Инициализируем класс книги"""
    def __init__(self):
        self.id='null'
        self.firstname = fake.first_name()
        self.lastname = fake.last_name()
        self.totalprice = fake.random_digit_not_null()
        self.depositpaid = 'true'
        self.checkin = fake.date(pattern="%Y-%m-%d")
        self.checkout = fake.date(pattern="%Y-%m-%d")
        self.additionalneeds = fake.phone_number()

    def get_fake_book(self):
        fake_book = {
            "firstname": self.firstname,
            "lastname": self.lastname,
            "totalprice": self.totalprice,
            "depositpaid": self.depositpaid,
            "bookingdates": {
                "checkin": self.checkin,
                "checkout": self.checkout
            },
            "additionalneeds": self.additionalneeds
        }
        return json.dumps(fake_book, indent=4)

    def set_book_id(self,book_id):
        self.id = book_id