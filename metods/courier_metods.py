import requests
from data import Urls, CourierData
from generate_random_courier import register_new_courier_and_return_login_password
import allure


class Courier:

    @allure.step("создать основного курьера")
    def post_reqest_create_base_courier(self):
        payload = CourierData.base_courier
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIER_URL}", json=payload, headers=headers)
        return response.status_code, response.json()

    @allure.step("создать рандомного курьера")
    def post_reqest_create_random_courier(self):
        courier_data, response = register_new_courier_and_return_login_password()
        payload = {"login": courier_data[0],
                   "password": courier_data[1],
                   "firstName": courier_data[2]}
        return response.status_code, response.json(), payload

    @allure.step("создать курьера с дефектными данными")
    def post_reqest_defective_create_courier(self, data):
        payload = data
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIER_URL}", json=payload, headers=headers)
        return response.status_code, response.json()

    @allure.step("создать курьера с повторным логином")
    def post_reqest_create_double_login_courier(self):
        payload = CourierData.registration_double_login_courier
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIER_URL}", json=payload, headers=headers)
        return [response.status_code, response.json()]

    @allure.step("вход основного курьера")
    def post_reqest_login_base_courier(self):
        payload = CourierData.login_base_courier
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIER_URL}/login", json=payload, headers=headers)
        return [response.status_code, response.json()]

    @allure.step("вход основного курьера без пароля")
    def post_reqest_login_base_courier_without_password(self):
        payload = CourierData.defective_data_login_base_courier
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIER_URL}/login", json=payload, headers=headers)
        return [response.status_code, response.json()]

    @allure.step("вход рандомного курьера")
    def post_reqest_login_random_courier(self):
        status_code, response_json, data = self.post_reqest_create_random_courier()
        payload = {"login": data["login"],
                   "password": data["password"]}
        headers = {"Content-Type" : "application/json"}
        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIER_URL}/login", json=payload, headers=headers)
        return response.status_code, response.json()['id']

    @allure.step("вход с дефектным логином курьера")
    def post_reqest_defective_login_courier(self, data):
        payload = data
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIER_URL}/login", json=payload, headers=headers)
        return [response.status_code, response.json()]

    @allure.step("вход курьера с повторным логином")
    def post_reqest_login_double_login_courier(self):
        payload = CourierData.ligin_double_login_courier
        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{Urls.BASE_URL}{Urls.COURIER_URL}/login", json=payload, headers=headers)
        return [response.status_code, response.json()]

    @allure.step("удалить курьера")
    def delite_reqest_delite_courier(self, id):
        response = requests.delete(f"{Urls.BASE_URL}{Urls.COURIER_URL}/{id}")
        return [response.status_code, response.json()]

    @allure.step("удалить курьера без его id")
    def delite_reqest_delite_courier_without_id(self):
        response = requests.delete(f"{Urls.BASE_URL}{Urls.COURIER_URL}")
        return [response.status_code, response.json()]

    @allure.step("удалить курьера с несуществующим id")
    def delite_reqest_delite_courier_with_nonexistent_id(self, id):
        response = requests.delete(f"{Urls.BASE_URL}{Urls.COURIER_URL}/{id}")
        return [response.status_code, response.json()]