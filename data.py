class TestAuthorizationData:
    REGISTRATION_COURIER_BODY = {
        "login": "petrushka",
        "password": "12345",
        "firstName": "petr"
    }

    REGISTRATION_COURIER_BODY_EMPTY_LOGIN = {
        "login": "",
        "password": "12345",
        "firstName": "petr"
    }

    REGISTRATION_COURIER_BODY_EMPTY_PASSWORD = {
        "login": "petrushka",
        "password": "",
        "firstName": "petr"
    }

    REGISTRATION_COURIER_BODY_EMPTY_FIRSTNAME = {
        "login": "petrushka1",
        "password": "123456",
        "firstName": ""
    }

    REGISTRATION_COURIER_BODY_NOT_ALL_FIELDS = {
        "login": "privet",
        "password": "123456"
    }

    LOGIN_COURIER_BODY_NOT_EXISTED = {
            "login": "eukfhajsdrlgiaf",
            "password": "riogekjfdnmc"
        }

    LOGIN_COURIER_BODY_EMPTY_LOGIN = {
            "login": "",
            "password": "riogekdnmvzcc"
        }

    LOGIN_COURIER_BODY_EMPTY_PASSWORD = {
            "login": "kfhalgiafkjsd",
            "password": ""
        }

    LOGIN_COURIER_BODY_NOT_ALL_FIELDS = {
        "password": ""
    }

class TestOrderData:

    ORDER_BODY_BLACK = {
        "firstName": "Сергей",
        "lastName": "Белов",
        "address": "Пр Мира, 142 - 7",
        "metroStation": 4,
        "phone": "+7 912 655 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-09-15",
        "comment": "нет",
        "color": ["BLACK"]}

    ORDER_BODY_GREY = {
        "firstName": "Иван",
        "lastName": "Петров",
        "address": "Ленина 198-45",
        "metroStation": 7,
        "phone": "+7 800 355 35 35",
        "rentTime": 3,
        "deliveryDate": "2024-09-30",
        "comment": "Привет",
        "color": ["GREY"]}

    ORDER_BODY_NO_COLOUR = {
        "firstName": "Иван",
        "lastName": "Петров",
        "address": "Ленина 198-45",
        "metroStation": 7,
        "phone": "+7 800 355 35 35",
        "rentTime": 3,
        "deliveryDate": "2024-09-30",
        "comment": "Привет",
        "color": []}

    ORDER_BODY_BLACK_GREY = {
        "firstName": "Иван",
        "lastName": "Петрович",
        "address": "Маркса 8-45",
        "metroStation": 2,
        "phone": "+7 300 355 55 75",
        "rentTime": 1,
        "deliveryDate": "2024-09-25",
        "comment": "Привет друг",
        "color": ["BLACK", "GREY"]}