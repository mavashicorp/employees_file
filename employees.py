# Напишите информационную систему «Сотрудники».
# Программа должна обеспечивать ввод данных, редакти-
# рование данных сотрудника, удаление сотрудника, поиск
# сотрудника по фамилии, вывод информации обо всех
# сотрудниках, указанного возраста, или фамилия которых
# начинается на указанную букву. Организуйте возможность
# сохранения найденной информации в файл. Также весь
# список сотрудников сохраняется в файл (при выходе из
# программы — автоматически, в процессе исполнения
# программы — по команде пользователя). При старте
# программы происходит загрузка списка сотрудников из
# указанного пользователем файла.

class Employee:
    def __init__(self, surname, name, age, position):
        self.surname = surname
        self.name = name
        self.age = age
        self.position = position
    
    def __str__(self):
        return f"{self.surname} {self.name}, {self.age} years old, {self.position}"


# функции для ввода данных, редактирования, удаления, поиска, вывода и сохранения\загрузки данных

# функция для добавления нового сотрудника
def add_employee(employees):
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    position = input("Введите должность: ")
    employees.append(Employee(surname, name, age, position))


# функция для редактирования данных сотрудника
def edit_employee(employees):
    surname = input("Введите фамилию сотрудника для редактирования: ")
    for employee in employees:
        if employee.surname == surname:
            employee.name = input("Введите новое имя: ")
            employee.age = int(input("Введите новый возраст: "))
            employee.position = input("Введите новую должность: ")
            print("Данные о сотрудниках обновлены")
            return
        print("Сотрудник не найден")


# функция для удаления сотрудника
def delete_employee(employees):
    surname = input("Введите фамилию сотрудника для удаления: ")
    for employee in employees:
        if employee.surname == surname:
            employees.remove(employee)
            print("Сотрудник удален")
            return
        print("Сотрудник не найден")


# поиск сотрудника по фамилии
def find_employee_by_last_name(employees):
    surname = input("Введите фамилию для поиска: ")
    for employee in employees:
        if employee.surname == surname:
            print(employee)
            return
        print("Сотрудник не найден")
    
        
# функция для вывода информации обо всех сотрудниках
def print_all_employees(employees):
    for employee in employees:
        print(employee)


