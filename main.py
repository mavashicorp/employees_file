# Основное меню и логика

from employee_operations import*
from file_operations import*

def main():
    employees = load_from_file("employees.json")
    while True:
        print("\n\tМеню:")
        print("\n1. Добавить сотрудника")
        print("\n2. Редактировать")
        print("\n3. Удалить")
        print("\n4. Найти сотрудника по фамилии")
        print("\n5. Показать всех сотрдников")
        print("\n6. Найти сотрудника во возрасту")
        print("\n7. Найти сотрудника по первой букве фамилии")
        print("\n8. Сохранить и выйти")
        print("\n9. Выйти без сохранения")
        
        choise = input("Enter your choise: ")
        
        if choise =='1':
            add_employee(employees)
        elif choise =='2':
            edit_employee(employees)
        elif choise =='3':
            delete_employee(employees)
        elif choise =='4':
            find_employee_by_last_name(employees)
        elif choise =='5':
            print_all_employees(employees)
        elif choise =='6':
            find_employees_by_age(employees)
        elif choise =='7':
            find_employees_by_first_letter(employees)
        elif choise =='8':
            save_to_file("employees.json", employees)
            break
        elif choise =='9':
            break
        else:
            print("Некорректный ввод. Попробуйте еще...")
            
        
main()