import requests as r
# Отправка POST запроса
res = r.post(
# URL эндпоинта для добавления сотрудника
url = "http://127.0.0.1:5000/add_employee",
# Данные сотрудника для отправки
data = {'name': '1212', "loc": "LOCATION #1"})


