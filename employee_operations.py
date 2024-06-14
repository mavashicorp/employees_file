
from employees import Employee


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
       


# поиск сотрудника по фамилии
def find_employee_by_last_name(employees):
    surname = input("Введите фамилию для поиска: ")
    found = False
    for employee in employees:
        if employee.surname == surname:
            print(employee)
            found = True
            break
    
    if not found:
        print("Сотрудник не найден")

      
    
        
# функция для вывода информации обо всех сотрудниках
def print_all_employees(employees):
    for employee in employees:
        print(employee)


# функция для поиска сотрудника по возрасту
def find_employees_by_age(employees):
    age = int(input("Введите возраст для поиска: "))
    for employee in employees:
        if employee.age == age:
            print(employee)


# функция для поиска сотрудника по первой букве
def find_employees_by_first_letter(employees):
    letter = input("Введите букву для поиска: ")
    for employee in employees:
        if employee.name[0].lower() == letter.lower():
            print(employee)


