from data import TestAuthorizationData
from helper import TestDataHelper
from samokat_api import SamokatApi
import allure

class TestLoginCourier:

    @allure.title('Проверка успешной авторизации курьера - код ответа 200')
    @allure.description(
        'Проверить успешность авторизации курьера: код ответа 200 - позитивный сценарий')
    def test_successful_login_courier_code(self, new_couriers_and_clear_courier_data):

        body = new_couriers_and_clear_courier_data['data']
        login_request = SamokatApi.login_courier(body)
        assert login_request.status_code == 200

    @allure.title('Проверка успешной авторизации курьера - с id курьера в ответе')
    @allure.description(
        'Проверить успешность авторизации курьера: с id курьера в ответе - позитивный сценарий')
    def test_successful_login_courier_message(self, new_couriers_and_clear_courier_data):

        body = new_couriers_and_clear_courier_data['data']
        login_request = SamokatApi.login_courier(body)
        try:
            courier_id = login_request.json()['id']
        except KeyError:
            courier_id = ""
        assert login_request.status_code == 200 and courier_id != ''


    @allure.title('Проверка НЕуспешной авторизации курьера с ошибкой в логине - код об ошибке 404')
    @allure.description(
        'Проверить НЕуспешность авторизации курьера с ошибкой в логине: код 404 об ошибке - негативный сценарий')
    def test_failed_mistake_login_courier_code(self, new_couriers_and_clear_courier_data):

        body = new_couriers_and_clear_courier_data['data']
        login_request = SamokatApi.login_courier(TestDataHelper.generate_mistake_login_courier_body(body))
        assert login_request.status_code == 404


    @allure.title('Проверка НЕуспешной авторизации курьера с ошибкой в логине')
    @allure.description(
        'Проверить НЕуспешность авторизации курьера с ошибкой в логине: сообщение об ошибке - негативный сценарий')
    def test_failed_mistake_login_courier_message(self, new_couriers_and_clear_courier_data):

        body = new_couriers_and_clear_courier_data['data']
        login_request = SamokatApi.login_courier(TestDataHelper.generate_mistake_login_courier_body(body))
        assert login_request.json()['message'] == "Учетная запись не найдена" and login_request.status_code == 404


    @allure.title('Проверка НЕуспешной авторизации курьера с ошибкой в пароле - код об ошибке 404')
    @allure.description(
        'Проверить НЕуспешность авторизации курьера с ошибкой в пароле: код 404 об ошибке - негативный сценарий')
    def test_failed_mistake_password_courier_code(self, new_couriers_and_clear_courier_data):

        body = new_couriers_and_clear_courier_data['data']
        login_request = SamokatApi.login_courier(TestDataHelper.generate_mistake_password_courier_body(body))
        assert login_request.status_code == 404

    @allure.title('Проверка НЕуспешной авторизации курьера с ошибкой в пароле')
    @allure.description(
        'Проверить НЕуспешность авторизации курьера с ошибкой в пароле: сообщение об ошибке - негативный сценарий')
    def test_failed_mistake_password_courier_message(self, new_couriers_and_clear_courier_data):

        body = new_couriers_and_clear_courier_data['data']
        login_request = SamokatApi.login_courier(TestDataHelper.generate_mistake_password_courier_body(body))
        assert login_request.status_code == 404 and login_request.json()['message'] == "Учетная запись не найдена"


    @allure.title('Проверка НЕуспешной авторизации незарегистрированного курьера - код об ошибке 404')
    @allure.description(
        'Проверить НЕуспешность авторизации незарегистрированного курьера: код 404 об ошибке - негативный сценарий')
    def test_failed_login_courier_not_existed_error_code(self):
        login_request = SamokatApi.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_NOT_EXISTED)
        assert login_request.status_code == 404

    @allure.title('Проверка НЕуспешной авторизации незарегистрированного курьера - сообщение об ошибке')
    @allure.description(
        'Проверить НЕуспешность авторизации незарегистрированного курьера : сообщение об ошибке - негативный сценарий')
    def test_failed_login_courier_not_existed_error_message(self):
        login_request = SamokatApi.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_NOT_EXISTED)
        assert login_request.json()['message'] == "Учетная запись не найдена" and login_request.status_code == 404

    @allure.title('Проверка НЕуспешной авторизации курьера без логина - код об ошибке 400')
    @allure.description(
        'Проверить НЕуспешность авторизации курьера без логина: код 400 об ошибке - негативный сценарий')
    def test_failed_login_courier_empty_login_error_code(self):
        login_request = SamokatApi.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_EMPTY_LOGIN)
        assert login_request.status_code == 400

    @allure.title('Проверка НЕуспешной авторизации курьера без логина')
    @allure.description(
        'Проверить НЕуспешность авторизации курьера без логина: сообщение об ошибке - негативный сценарий')
    def test_failed_login_courier_empty_login_error_message(self):

        login_request = SamokatApi.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_EMPTY_LOGIN)
        assert login_request.json()['message'] == "Недостаточно данных для входа" and login_request.status_code == 400

    @allure.title('Проверка НЕуспешной авторизации курьера без пароля - код об ошибке 400')
    @allure.description(
        'Проверить НЕуспешность авторизации курьера без пароля: код 400 об ошибке - негативный сценарий')
    def test_failed_login_courier_empty_password_error_code(self):

        login_request = SamokatApi.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_EMPTY_PASSWORD)
        assert login_request.status_code == 400

    @allure.title('Проверка НЕуспешной авторизации курьера без пароля')
    @allure.description(
        'Проверить НЕуспешность авторизации курьера без пароля: сообщение об ошибке - негативный сценарий')
    def test_failed_login_courier_empty_password_error_message(self):

        login_request = SamokatApi.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_EMPTY_PASSWORD)
        assert login_request.json()['message'] == "Недостаточно данных для входа" and login_request.status_code == 400

    @allure.title('Проверка НЕуспешной авторизации курьера с передачей в запрос не всех обязательных полей')
    @allure.description(
        'Проверить НЕуспешность авторизации курьера с передачей в запрос не всех обязательных полей: код ответа не 201 - негативный сценарий')
    def test_failed_login_courier_not_all_fields(self):

        login_request = SamokatApi.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_NOT_ALL_FIELDS)
        assert login_request.status_code != 201