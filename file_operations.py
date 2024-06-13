
# функции для ввода данных, редактирования, удаления, поиска, вывода и сохранения\загрузки данных

import json
from employees import Employee


# функция для сохранения в файл
def save_to_file(employees, filename):
    data = [emp.to_dict() for emp in employees]
    with open(filename, 'w') as file:
        json.dump(data, file)
        
# функция для загрузки из файла
def load_from_file(employees):
    try:
        with open('employees.json', 'r') as file:
            data = json.load(file)
            for emp in data:
                employees.append(Employee(**emp))
    except FileNotFoundError:
                print("Файл не найден, пустой список сотрудников")
                return[]