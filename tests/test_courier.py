import pytest
from metods.courier_metods import Courier
from data import CourierData
import allure


class TestCourierCreate:

    @allure.description("Тест по созданию рандомного курьера")
    @allure.title("Создать курьера")
    def test_create_courier(self):
        courier = Courier()
        status_code, response_context, payload = courier.post_reqest_create_random_courier()
        assert status_code == 201 and str(response_context.get("ok")) == 'True'

    @allure.description("Тест по созданию курьеров с одинаковыми логинами")
    @allure.title("Создать курьера с одинаковыми логинами")
    def test_double_create_courier(self):
        courier = Courier()
        response_one = courier.post_reqest_create_double_login_courier()
        status_code, response_context = courier.post_reqest_create_double_login_courier()
        status, id_courier = courier.post_reqest_login_double_login_courier()
        courier.delite_reqest_delite_courier(id_courier['id'])
        assert status_code == 409 and response_context

    @allure.description("Тест по созданию курьеров с дефектными данными")
    @allure.title("Создать курьера с дефектными данными")
    @pytest.mark.parametrize('data', [CourierData.defective_data_for_create_courier_1])
    def test_defective_create_courier(self, data):
        courier = Courier()
        status_code, response_context = courier.post_reqest_defective_create_courier(data)
        assert status_code == 400 and response_context

    @allure.description("Тест по созданию курьера")
    @allure.title("Создать базового курьера")
    def test_create_base_courier(self):
        courier = Courier()
        status_code, response_context = courier.post_reqest_create_base_courier()
        login_courier, id_courier = courier.post_reqest_login_base_courier()
        courier.delite_reqest_delite_courier(id_courier["id"])
        assert status_code == 201 and str(response_context.get("ok")) == 'True'


class TestDeleteCourier:

    @allure.description("Тест по удалению курьера")
    @allure.title("Удалить курьера ")
    def test_delete_courier(self):
        courier = Courier()
        courier.post_reqest_create_base_courier()
        login_courier, id_courier = courier.post_reqest_login_base_courier()
        status_code, response_context = courier.delite_reqest_delite_courier(id_courier['id'])
        assert status_code == 200 and response_context

    @allure.description("Тест по удалению курьера без id")
    @allure.title("Удалить курьера без id")
    def test_delete_courier_without_id(self):
        courier = Courier()
        courier.post_reqest_create_base_courier()
        login_courier, id_courier = courier.post_reqest_login_base_courier()
        status_code, response_context = courier.delite_reqest_delite_courier_without_id()
        assert status_code == 404 and response_context

    @allure.description("Тест по удалению курьера с несуществующим id")
    @allure.title("Удалить курьера с несуществующим id")
    def test_delete_courier_with_nonexistent_id(self):
        courier = Courier()
        courier.post_reqest_create_base_courier()
        login_courier, id_courier = courier.post_reqest_login_base_courier()
        status_code, response_context = courier.delite_reqest_delite_courier_with_nonexistent_id(99999999)
        courier.delite_reqest_delite_courier(id_courier["id"])
        assert status_code == 404 and response_context


class TestLoginCourier:

    @allure.description("Тест по входу курьера")
    @allure.title("Вход курьера")
    def test_login_random_courier(self):
        courier = Courier()
        status_code, id = courier.post_reqest_login_random_courier()
        assert status_code == 200 and id is not None

    @allure.description("Тест по входу курьера с дефектными данными")
    @allure.title("Вход курьера с дефектными данными")
    @pytest.mark.parametrize('data', [CourierData.non_existent_login_courier,
                                      CourierData.defective_password_for_login_base_courier])
    def test_defective_login_courier(self, data):
        courier = Courier()
        status_code, response_context = courier.post_reqest_defective_login_courier(data)
        assert status_code == 404 and response_context

    @allure.description("Тест по входу курьера без пароля")
    @allure.title("Вход курьера без парол")
    def test_login_base_courier_without_password(self):
        courier = Courier()
        status_code1, json1 = courier.post_reqest_create_base_courier()
        status_code1, json1 = courier.post_reqest_login_base_courier_without_password()
        status_code_login, courier_id = courier.post_reqest_login_base_courier()
        courier.delite_reqest_delite_courier(courier_id)
        assert status_code1 == 400

