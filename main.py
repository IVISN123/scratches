from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Инициализация Flask приложения
app = Flask(__name__)
# Конфигурация базы данных SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees_pos.db'
# Инициализация SQLAlchemy
db = SQLAlchemy(app)

# Определение модели Employee
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))docker
    loc = db.Column(db.String(50))

    # Конструктор класса Employee
    def __init__(self, name, loc):
        self.name = name
        self.loc = loc

# Создание таблицы employees, если её нет
with app.app_context():
    db.create_all()

# Маршрут для добавления нового сотрудника
@app.route('/add_employee', methods=['POST'])
def add_employee():
    name = request.form['name']
    loc = request.form['loc']
    employee = Employee(name, loc)
    db.session.add(employee)
    db.session.commit()
    return {"session": "Employee and location added successfully"}

# Маршрут для обновления локации сотрудника
@app.route('/upd_employee_loc/<int:id>', methods=['POST'])
def upd_employee_loc(id):
    employee = Employee.query.get(id)
    if employee:
        loc = request.form['loc']
        employee.loc = loc  # Обновляем поле loc
        db.session.commit()  # Сохраняем изменения
        return {"session": "Employee location updated successfully"}
    else:
        return {'Error': 'Employee not found'}

# Маршрут для получения данных о сотруднике по ID
@app.route('/get_employee/<int:id>')
def get_employee(id):
    employee = Employee.query.get(id)
    if employee:
        return jsonify({
            'id': employee.id,
            'name': employee.name,
            'loc': employee.loc
        })
    else:
        return {'Error': 'Employee not found'}

# Маршрут для отображения главной страницы
@app.route('/')
def index():
    return render_template('index.html')

# Запуск приложения
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

