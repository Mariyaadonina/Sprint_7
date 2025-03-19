from faker import Faker
from data import TestAuthorizationData
import allure

class TestDataHelper:

    @allure.step('Сформировать рандомные данные для регистрации нового курьера')
    def generate_registration_body():
        fake = Faker()
        body = TestAuthorizationData.REGISTRATION_COURIER_BODY.copy()
        body['login'] = fake.user_name()
        return body

    @allure.step('Получить данные для авторизации зарегистрированного курьера из данных регистрации')
    def generate_login_courier_body(body):
        del body['firstName']
        return body

    @allure.step('Сформировать данные зарегистрированного курьера с ошибкой в логине')
    def generate_mistake_login_courier_body(body):
        body['login'] = body['login'] + '1'
        return body

    @allure.step('Сформировать данные зарегистрированного курьера с ошибкой в пароле')
    def generate_mistake_password_courier_body(body):
        body['password'] = body['password'] + '1'
        return body

