# Основное меню и логика

from employee_operations import*
from file_operations import*

def main():
    employees = load_from_file("employees.txt")
    while True:
        print("\n\tМеню:")
        print("\n1. Добавить сотрудника")
        print("\n2. Редактировать")
        print("\n3. Удалить")
        print("\n4. Найти сотрудника по фамилии")
        print("\n5. Показать всех сотрдников")
        print("\n6. Найти сотрудника во возрасту")
        print("\n7. Найти сотрудника по первой букве имени\фамилии")
        print("\n8. Сохранить и выйти")
        print("\n9. Выйти без сохранения")
        
        choise = input("\n\tВыберите действие: ")
        
        if choise =='1':
            add_employee(employees)
            #ok
        elif choise =='2':
            edit_employee(employees)
            #ok
        elif choise =='3':
            delete_employee(employees)
            #ok чувствителен к регистру
        elif choise =='4':
            find_employee_by_last_name(employees)
            #ok
        elif choise =='5':
            print_all_employees(employees)
            #ok
        elif choise =='6':
            find_employees_by_age(employees)
            #ok
        elif choise =='7':
            find_employees_by_first_letter(employees)
            #ok
        elif choise =='8':
            save_to_file("employees.txt", employees)
            #ok
            break
        elif choise =='9':
            break
            #ok
        else:
            print("Некорректный ввод. Попробуйте еще...")
            
        
# для определения, запущен ли текущий скрипт напрямую из командной строки или
# файл интерпретируется как модуль для импорта в другой скрипт.
if __name__ == "__main__":
    main()