
class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
    ORDER_URL = 'orders'
    COURIER_URL = 'courier'


class CourierData:
    base_courier = {"login": "lololo",
                    "password": "1234",
                    "firstName": "lololo"}

    login_base_courier = {"login": "lololo",
                          "password": "1234"}

    defective_password_for_login_base_courier = {"login": "lololo",
                                                 "password": "1235"}

    defective_data_login_base_courier = {"login": "lololo",
                                         "password": ""}

    defective_data_for_create_courier_1 = {"login": "lalalala",
                                         "password": ""}

    defective_data_for_create_courier_2 = {"login": "lalalal",
                                         "password": "1234"}

    non_existent_login_courier = {"login": "nonexistent_login",
                                  "password": "1234"}

    registration_double_login_courier = {"login": "lolola",
                                         "password": "1235",
                                         "firstName": "lolola"}

    ligin_double_login_courier = {"login": "lolola",
                                  "password": "1235"}



class OrderData:
    ORDER_DATA_1 = {"firstName": "Naruto",
               "lastName": "Uchiha",
               "address": "Konoha, 142 apt.",
               "metroStation": 1,
               "phone": "+7 800 355 35 35",
               "rentTime": 1,
               "deliveryDate": "2024-11-10",
               "comment": "Saske, come back to",
               "color": ["BLACK"]}

    ORDER_DATA_2 = {"firstName": "Narutoo",
               "lastName": "Uchihaa",
               "address": "Konoha, 142 apt.",
               "metroStation": 2,
               "phone": "+7 800 355 35 36",
               "rentTime": 2,
               "deliveryDate": "2024-11-10",
               "comment": "Saske, come back too",
               "color": ["BLACK", "GREY"]}

    ORDER_DATA_3 = {"firstName": "Narutoo",
               "lastName": "Uchihaa",
               "address": "Konoha, 142 apt.",
               "metroStation": 2,
               "phone": "+7 800 355 35 36",
               "rentTime": 2,
               "deliveryDate": "2024-11-10",
               "comment": "Saske, come back too"}

