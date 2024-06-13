
# класс Employee

class Employee:
    def __init__(self, surname, name, age, position):
        self.surname = surname
        self.name = name
        self.age = age
        self.position = position
    
    def __str__(self):
        return f"{self.surname} {self.name}, {self.age} лет, {self.position}"

