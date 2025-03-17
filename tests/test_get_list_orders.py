from data import TestOrderData
from samokat_api import SamokatApi
import allure

class TestGetListOrders:

    @allure.title('Проверка успешного получения списка всех заказов - корректный код ответа')
    @allure.description('Проверить успешность получения списка всех заказов: код ответа 200 - позитивный сценарий')
    def test_successful_get_list_orders_code(self, new_couriers_and_clear_courier_data):

        order_request = SamokatApi.create_order(TestOrderData.ORDER_BODY_BLACK)
        order_track1 = order_request.json()['track']
        order_request = SamokatApi.create_order(TestOrderData.ORDER_BODY_GREY)
        order_track2 = order_request.json()['track']
        order_request = SamokatApi.create_order(TestOrderData.ORDER_BODY_NO_COLOUR)
        order_track3 = order_request.json()['track']

        list_orders_request = SamokatApi.get_list_orders()

        assert list_orders_request.status_code == 200
        SamokatApi.cancel_order(order_track1)
        SamokatApi.cancel_order(order_track2)
        SamokatApi.cancel_order(order_track3)

    @allure.title('Проверка успешного получения списка всех заказов - корректное сообщение')
    @allure.description('Проверить успешность получения списка всех заказов: приходит сообщение со списком заказов - позитивный сценарий')
    def test_successful_get_list_orders_message(self, new_couriers_and_clear_courier_data):

        order_request = SamokatApi.create_order(TestOrderData.ORDER_BODY_BLACK)
        order_track1 = order_request.json()['track']
        order_request = SamokatApi.create_order(TestOrderData.ORDER_BODY_GREY)
        order_track2 = order_request.json()['track']

        list_orders_request = SamokatApi.get_list_orders()

        assert list_orders_request.json()['orders'] != [] and list_orders_request.status_code == 200

        SamokatApi.cancel_order(order_track1)
        SamokatApi.cancel_order(order_track2)