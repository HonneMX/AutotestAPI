import os

class Enviroment():
    DEV = 'dev'
    QA = 'qa'
    STAGE= 'stage'
    PROD = 'prod'

    URLS = {
        DEV: 'https://restful-booker.herokuapp.com',
        QA : 'https://restful-booker.herokuapp.com',
        STAGE: 'https://restful-booker.herokuapp.com',
        PROD:'https://restful-booker.herokuapp.com'
    }

    def __init__(self):
        try:
            self.env = os.environ['ENV']
        except KeyError:
            self.env = self.DEV

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Unknown value of ENV variable {self.env}")

ENV_ONJECT = Enviroment()