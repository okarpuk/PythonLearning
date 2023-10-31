# Объект без параметров и метод без параметров
class Person:
    def __init__(self):
        print("Object created")

    def say_hello(self):
        print("Hello")

tom = Person()
tom.say_hello()


# Объект без параметров и метод с параметрами
class Person:
    def say(self, message):
        print(message)

tom = Person()
tom.say("hello, Tom")


# Обращение к функциональности через self
class Person:
    def say_1(self, message):
        print(message)

    def say_2(self):
        self.say_1("Hello Tom 2")

tom = Person()
tom.say_2()

# Создание объекта через конструктор с атрибутами
class Person:
    def __init__(self, name):
        self.name = name
        self.age = 20

tom = Person("Tom Soyer")
print(tom.name)
print(tom.age)

tom.age = 40
print(tom.age)

tom.company = "Apple"
print(tom.company)


# Обращение к атрибутам объекта через Self
