from helper import TestDataHelper
from samokat_api import SamokatApi
from data import TestAuthorizationData
import allure

class TestRegistrationCoruier:

    @allure.title('Проверка успешной регистрации нового курьера - корректный код ответа')
    @allure.description('Проверить успешность регистрации нового курьера: код ответа 201 - позитивный сценарий')
    def test_successful_registration_courier_correct_code(self):

        body = TestDataHelper.generate_registration_body()
        registration_request = SamokatApi.registration_courier(body)
        login_request = SamokatApi.login_courier(TestDataHelper.generate_login_courier_body(body))
        try:
            courier_id = login_request.json()['id']
        except KeyError:
            courier_id = ""

        assert registration_request.status_code == 201
        SamokatApi.delete_courier(courier_id)

    @allure.title('Проверка успешной регистрации нового курьера - корректное тело ответа')
    @allure.description('Проверить успешность регистрации нового курьера: тело ответа {"ok":True} - позитивный сценарий')
    def test_successful_registration_courier_correct_message(self):

        body = TestDataHelper.generate_registration_body()
        registration_request = SamokatApi.registration_courier(body)
        login_request = SamokatApi.login_courier(TestDataHelper.generate_login_courier_body(body))
        try:
            courier_id = login_request.json()['id']
        except KeyError:
            courier_id = ""

        assert registration_request.json()['ok'] == True and registration_request.status_code == 201
        SamokatApi.delete_courier(courier_id)

    @allure.title('Проверка НЕуспешной регистрации курьера с уже существующими данными - корректный код ошибки')
    @allure.description('Проверить НЕуспешность регистрации нового курьера: код ответа 409 - негативный сценарий')
    def test_failed_registration_courier_existed_error_code(self, new_couriers_and_clear_courier_data):

        body = new_couriers_and_clear_courier_data['data']
        registration_request_double = SamokatApi.registration_courier(body)
        assert registration_request_double.status_code == 409

    @allure.title('Проверка НЕуспешной регистрации нового курьера с уже существующими данными - корректный текст ошибки')
    @allure.description('Проверить НЕуспешность регистрации нового курьера с уже существующими данными: текст ошибки {"message":"Этот логин уже используется"}- негативный сценарий')
    def test_failed_registration_courier_existed_error_message(self, new_couriers_and_clear_courier_data):

        body = new_couriers_and_clear_courier_data['data']
        registration_request_double = SamokatApi.registration_courier(body)
        assert registration_request_double.json()["message"] == "Этот логин уже используется" and registration_request_double.status_code == 409

    @allure.title('Проверка НЕуспешной регистрации нового курьера с пустым логином - корректный код ошибки')
    @allure.description('Проверить НЕуспешность регистрации нового курьера с пустым логином: код ответа 400 - негативный сценарий')
    def test_failed_registration_courier_empty_login_error_code(self):

        registration_request = SamokatApi.registration_courier(TestAuthorizationData.REGISTRATION_COURIER_BODY_EMPTY_LOGIN)
        assert registration_request.status_code == 400

    @allure.title('Проверка НЕуспешной регистрации нового курьера с пустым логином - корректный текст ошибки')
    @allure.description('Проверить НЕуспешность регистрации нового курьера с пустым логином: текст ошибки {"message":"Недостаточно данных для создания учетной записи"}- негативный сценарий')
    def test_failed_registration_courier_empty_login_error_message(self):

        registration_request = SamokatApi.registration_courier(TestAuthorizationData.REGISTRATION_COURIER_BODY_EMPTY_LOGIN)
        assert registration_request.json()["message"] == "Недостаточно данных для создания учетной записи" and registration_request.status_code == 400

    @allure.title('Проверка НЕуспешной регистрации нового курьера с пустым паролем - корректный код ошибки')
    @allure.description('Проверить НЕуспешность регистрации нового курьера с пустым паролем: код ответа 400 - негативный сценарий')
    def test_failed_registration_courier_empty_password_error_code(self):
        registration_request = SamokatApi.registration_courier(TestAuthorizationData.REGISTRATION_COURIER_BODY_EMPTY_PASSWORD)
        assert registration_request.status_code == 400

    @allure.title('Проверка НЕуспешной регистрации нового курьера с пустым паролем - корректный текст ошибки')
    @allure.description('Проверить НЕуспешность регистрации нового курьера с пустым паролем: текст ошибки {"message":"Недостаточно данных для создания учетной записи"}- негативный сценарий')
    def test_failed_registration_courier_empty_password_error_message(self):
        registration_request = SamokatApi.registration_courier(TestAuthorizationData.REGISTRATION_COURIER_BODY_EMPTY_PASSWORD)
        assert registration_request.json()["message"] == "Недостаточно данных для создания учетной записи" and registration_request.status_code == 400

    @allure.title('Проверка НЕуспешной регистрации нового курьера с пустым именем')
    @allure.description('Проверить НЕуспешность регистрации нового курьера с пустым именем: код ответа не 201 - негативный сценарий')
    def test_failed_registration_courier_empty_firstname_error_code(self):
        registration_request = SamokatApi.registration_courier(TestAuthorizationData.REGISTRATION_COURIER_BODY_EMPTY_FIRSTNAME)
        assert registration_request.status_code != 201

    @allure.title('Проверка НЕуспешной регистрации нового курьера с передачей в запрос не всех обязательных полей')
    @allure.description('Проверить НЕуспешность регистрации нового курьера с передачей в запрос не всех обязательных полей: код ответа не 201 - негативный сценарий')
    def test_failed_registration_courier_not_all_fields(self):
        registration_request = SamokatApi.registration_courier(TestAuthorizationData.REGISTRATION_COURIER_BODY_NOT_ALL_FIELDS)
        assert registration_request.status_code != 201

