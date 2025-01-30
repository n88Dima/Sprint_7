class Urls:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru'
    LOGIN_COURIER_URL = f"{MAIN_URL}/api/v1/courier/login"
    CREATE_COURIER_URL = f"{MAIN_URL}/api/v1/courier"
    DELETE_COURIER_URL = f"{MAIN_URL}/api/v1/courier/:id"
    CREATE_ORDERD_URL = f"{MAIN_URL}/api/v1/orders"