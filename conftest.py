import pytest
from helper import TestDataHelper
from samokat_api import SamokatApi
import allure

@allure.step('Фикстура: Регистрация нового курьера, его логин в системе, удаление курьера после выполнения теста')
@pytest.fixture(scope = 'function')
def new_couriers_and_clear_courier_data():

    # регистрация курьера
    body = TestDataHelper.generate_registration_body()
    registration_request = SamokatApi.registration_courier(body)

    # логин курьера и получение его айди
    login_request = SamokatApi.login_courier(TestDataHelper.generate_login_courier_body(body))
    try:
        courier_id = login_request.json()['id']
    except KeyError:
        courier_id = ""

    # формирование данных курьера
    courier_data = {
                    "data" : body,
                    "status_code_reg" : registration_request.status_code,
                    "message_reg" : registration_request.text,
                    "courier_id" : login_request.json()['id'],
                    "status_code_login" : login_request.status_code,
                    "message_login" : login_request.text}

    yield courier_data

    # удаление курьера
    SamokatApi.delete_courier(courier_id)


@allure.step('Фикстура: Создание заказа, удаление заказа после выполнения теста')
@pytest.fixture(scope='function')
def cancel_order_fixture():
    order_track_data = {}

    yield order_track_data

    if 'track' in order_track_data:
        SamokatApi.cancel_order(order_track_data['track'])