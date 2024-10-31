import pytest
from metods.order_metods import Order
from data import CourierData, OrderData
from metods.courier_metods import Courier
import allure


class TestOrderCreate:

    @allure.description("Параметризованный тест, для проверки создания заказа с различными данными")
    @allure.title("Создание заказа")
    @pytest.mark.parametrize('data', [OrderData.ORDER_DATA_1,
                                      OrderData.ORDER_DATA_2,
                                      OrderData.ORDER_DATA_3])
    def test_create_order(self, data):
        order = Order()
        status_code, response_context = order.post_reqest_order(data)
        assert status_code == 201 and response_context


class TestGetOrder:

    @allure.description("Тест по получению данных заказа")
    @allure.title("Получить данных заказа")
    def test_get_order(self):
        order = Order()
        status, track = order.post_reqest_order(OrderData.ORDER_DATA_1)
        status_code, response_context = order.get_reqest_get_order(track["track"])
        assert status_code == 200 and response_context

    @allure.description("Тест по получению данных заказа, при вводе несуществующего трека заказа")
    @allure.title("Получить данных заказа")
    def test_get_order_with_nonexistent_track(self):
        order = Order()
        status_code, response_context = order.get_reqest_get_order(999999999)
        assert status_code == 404 and response_context

    @allure.description("Тест по получению данных зо всех заказах")
    @allure.title("Получить списка заказов")
    def test_get_list_orders(self):
        order = Order()
        status_code, response_context = order.get_reqest_get_list_orders()
        assert status_code == 200 and response_context


class TestTakeOrder:


    """здесь тест падает, пишет, что нет такого заказа, но трек я получаю и подставляю верно,
    возможно это связано с тем что не успевает отрабатработать база"""
    @allure.description("Тест по приемке заказа")
    @allure.title("Принять заказ")
    def test_take_order(self):
        courier = Courier()
        courier.post_reqest_create_base_courier()
        login_courier, id_courier = courier.post_reqest_login_base_courier()
        order = Order()
        status, track = order.post_reqest_order(OrderData.ORDER_DATA_1)
        status_code, response_context = order.put_reqest_take_orders(track["track"], id_courier['id'])
        courier.delite_reqest_delite_courier(id_courier['id'])
        assert status_code == 200 and str(response_context.get("ok")) == 'True'

    @allure.description("Тест по приемке заказа, без введения трека заказа")
    @allure.title("Принять заказ, без трека")
    def test_take_order_without_track(self):
        courier = Courier()
        courier.post_reqest_create_base_courier()
        login_courier, id_courier = courier.post_reqest_login_base_courier()
        order = Order()
        status, track = order.post_reqest_order(OrderData.ORDER_DATA_1)
        status_code, response_context = order.put_reqest_take_orders_without_track(id_courier['id'])
        courier.delite_reqest_delite_courier(id_courier['id'])
        assert status_code == 404

    @allure.description("Тест по приемке заказа, без введения id курьера")
    @allure.title("Принять заказ, без id курьера")
    def test_take_order_without_id_courier(self):
        courier = Courier()
        courier.post_reqest_create_base_courier()
        login_courier, id_courier = courier.post_reqest_login_base_courier()
        order = Order()
        status, track = order.post_reqest_order(OrderData.ORDER_DATA_1)
        status_code, response_context = order.put_reqest_take_orders_without_id_courier(track["track"])
        courier.delite_reqest_delite_courier(id_courier['id'])
        assert status_code == 400

    @allure.description("Тест по приемке заказа, с введением номера несуществующего заказа")
    @allure.title("Принять заказ, с несуществующим номером")
    def test_take_order_without_bad_track(self):
        courier = Courier()
        courier.post_reqest_create_base_courier()
        login_courier, id_courier = courier.post_reqest_login_base_courier()
        order = Order()
        status, track = order.post_reqest_order(OrderData.ORDER_DATA_1)
        status_code, response_context = order.put_reqest_take_orders(9999999, id_courier['id'])
        courier.delite_reqest_delite_courier(id_courier['id'])
        assert status_code == 404

    @allure.description("Тест по приемке заказа, с несуществующими данными")
    @allure.title("Принять заказ, с несуществующими данными")
    def test_take_order_without_bad_id_courier(self):
        courier = Courier()
        courier.post_reqest_create_base_courier()
        login_courier, id_courier = courier.post_reqest_login_base_courier()
        order = Order()
        status, track = order.post_reqest_order(OrderData.ORDER_DATA_1)
        status_code, response_context = order.put_reqest_take_orders(9999999, 9999999)
        courier.delite_reqest_delite_courier(id_courier['id'])
        assert status_code == 404
