class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 50

    def set_age(self, age):
        if 1 < age < 100:
            self.__age = age
        else:
            print("Invalid age")

    def get_age(self):
        return self.__age

    def display_info(self):
        print(f"Имя: {self.__name}, Возраст: {self.__age}")

antonio = Person("Antonio")
antonio.set_age(98)
antonio.display_info()
print(antonio.get_age())

