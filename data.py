from faker import Faker

fake = Faker()

class Errors:
    COURIER_LOGIN_EMPTY_DATA = "Недостаточно данных для входа"
    COURIER_CREATE_EMPTY_DATA = "Недостаточно данных для создания учетной записи"   
    COURIER_ALREADY_CREATED = "Этот логин уже используется"
    COURIER_CREATE_DONT_HAVE_REQURED_FIELDS = "Недостаточно данных для создания учетной записи"
    COURIER_LOGIN_FAIL_AUTH = "Учетная запись не найдена"

class Payloads:

    def generate_courier_payload():
        return {
        "login": fake.user_name(),
        "password": "1234",
        "firstName": "Dmitry"
    }

    ALREADY_REGISTERED_COURIER = {
    "login": "Dmitry",
    "password": "1234",
    "firstName": "Dmitry"
    }

    ORDER_COLOR_BLACK = {
        "firstName": "Dmitry",
        "lastName": "Terekhov",
        "address": "Кантемировская 4к3",
        "metroStation": 1,
        "phone": "+79661479944",
        "rentTime": 10,
        "deliveryDate": "2025-06-22",
        "comment": "Позвонить за 5 минут до доставки",
        "color": [
            "BLACK"
        ]
    }

    ORDER_COLOR_GRAY = {
        "firstName": "Dmitry",
        "lastName": "Terekhov",
        "address": "Кантемировская 4к3",
        "metroStation": 1,
        "phone": "+79661479944",
        "rentTime": 10,
        "deliveryDate": "2025-06-22",
        "comment": "Позвонить за 5 минут до доставки",
        "color": [
            "GRAY"
        ]
    }
    ORDER_COLOR_BLACK_AND_GRAY = {
        "firstName": "Dmitry",
        "lastName": "Terekhov",
        "address": "Кантемировская 4к3",
        "metroStation": 1,
        "phone": "+79661479944",
        "rentTime": 10,
        "deliveryDate": "2025-06-22",
        "comment": "Позвонить за 5 минут до доставки",
        "color": [
            "BLACK",
            "GRAY"
        ]
    }
    ORDER_WITHOUT_COLOR = {
        "firstName": "Dmitry",
        "lastName": "Terekhov",
        "address": "Кантемировская 4к3",
        "metroStation": 1,
        "phone": "+79661479944",
        "rentTime": 10,
        "deliveryDate": "2025-06-22",
        "comment": "Позвонить за 5 минут до доставки",
        "color": []
    }