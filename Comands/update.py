import requests as r
# Отправка POST запроса

# URL эндпоинта для добавления сотрудника
url = "http://127.0.0.1:5000/upd_employee_loc/1"
# Данные сотрудника для отправки
data = {'loc': 'New Location'}
# Отправка POST запроса
res = r.post(url, data=data)