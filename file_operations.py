
# функции для ввода данных, редактирования, удаления, поиска, вывода и сохранения\загрузки данных

import json
from employees import Employee


def save_to_file(filename, employees):
    with open(filename, 'w', encoding='utf-8') as file:
        for emp in employees:
            file.write(f"{emp.surname},{emp.name},{emp.age},{emp.position}\n")




def load_from_file(filename):
    employees = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            data = line.strip().split(',')
            if len(data) == 4:
                employees.append(Employee(data[0], data[1], int(data[2]), data[3]))
    return employees



# def save_to_file(employees, filename):
#     data = [emp.__dict__ for emp in employees]
#     with open(filename, 'w') as file:
#         json.dump(data, file)


# def load_from_file(filename):
#     try:
#         with open(filename, 'r') as file:
#             data = json.load(file)
#             return [Employee(**emp) for emp in data]
#     except FileNotFoundError:
#         print("File not found, starting with an empty employee list.")
#         return []