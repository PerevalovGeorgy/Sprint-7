from requests import post, get, put
from data import Urls
import allure

class Order:
    @allure.step("создать заказ, и получить номер заказа")
    def post_reqest_order(self, payload):
        response = post(f"{Urls.BASE_URL}{Urls.ORDER_URL}", json=payload)
        return response.status_code, response.json()

    @allure.step("получить список заказов")
    def get_reqest_get_list_orders(self):
        response = get(f"{Urls.BASE_URL}{Urls.ORDER_URL}")
        return response.status_code, response.json()

    @allure.step("принять заказ")
    def put_reqest_take_orders(self, id_order, id_courier):
        response = put(f"{Urls.BASE_URL}{Urls.ORDER_URL}/accept/{id_order}?courierId={id_courier}")
        return response.status_code, response.json()

    @allure.step("принять заказ без трека")
    def put_reqest_take_orders_without_track(self,  id_courier):
        response = put(f"{Urls.BASE_URL}{Urls.ORDER_URL}/accept/?courierId={id_courier}")
        return response.status_code, response.json()

    @allure.step("принять заказ без id  курьера")
    def put_reqest_take_orders_without_id_courier(self,  id_order):
        response = put(f"{Urls.BASE_URL}{Urls.ORDER_URL}/accept/{id_order}")
        return response.status_code, response.json()

    @allure.step("получить данные заказа")
    def get_reqest_get_order(self, track):
        response = get(f"{Urls.BASE_URL}{Urls.ORDER_URL}/track?t={track}")
        return response.status_code, response.json()

