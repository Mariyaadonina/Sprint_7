from data import TestOrderData
from samokat_api import SamokatApi
import pytest
import allure

class TestCreateOrder:

    @allure.title('Проверка успешного создания заказа - корректный код ответа')
    @allure.description('Проверить успешность создания заказа с разными вариантами цвета самоката (черный, серый, черный и серый, цвет не выбран): код ответа 201 - позитивный сценарий')
    @pytest.mark.parametrize('order_body',
                             [TestOrderData.ORDER_BODY_BLACK, TestOrderData.ORDER_BODY_GREY,
                              TestOrderData.ORDER_BODY_BLACK_GREY, TestOrderData.ORDER_BODY_NO_COLOUR])
    def test_successful_create_order_code(self, order_body, new_couriers_and_clear_courier_data):

        order_request = SamokatApi.create_order(order_body)
        order_track = order_request.json()['track']
        assert order_request.status_code == 201

        SamokatApi.cancel_order(order_track)

    @allure.title('Проверка успешного создания заказа - в ответе приходит track - номер заказа')
    @allure.description('Проверить успешность создания заказа с разными вариантами цвета самоката (черный, серый, черный и серый, цвет не выбран): сообщение с номеом заказа track - позитивный сценарий')
    @pytest.mark.parametrize('order_body',
                             [TestOrderData.ORDER_BODY_BLACK, TestOrderData.ORDER_BODY_GREY,
                              TestOrderData.ORDER_BODY_BLACK_GREY, TestOrderData.ORDER_BODY_NO_COLOUR])
    def test_successful_create_order_message(self, order_body, new_couriers_and_clear_courier_data):

        order_request = SamokatApi.create_order(order_body)
        order_track = order_request.json()['track']
        assert order_request.json()['track'] != "" and order_request.status_code == 201

        SamokatApi.cancel_order(order_track)