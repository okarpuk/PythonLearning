class Car:
    def __init__(self, model, year, engine_volume, price, mileage, wheels=4):
        self.model = model
        self.year = year
        self.engine_volume = engine_volume
        self.price = price
        self.mileage = mileage
        self.wheels = wheels

    def description(self):
        return f"Модель: {self.model}, Год выпуска: {self.year}, Объем двигателя: {self.engine_volume}, Цена: {self.price}, Пробег: {self.mileage}, Количество колес: {self.wheels}"

car1 = Car("Toyota Corolla", 2020, 1.8, 20000, 15000)

class Truck(Car):
    def __init__(self, model, year, engine_volume, price, mileage, wheels=8):
        super().__init__(model, year, engine_volume, price, mileage, wheels)

truck1 = Truck("Volvo FH", 2018, 12.8, 80000, 50000)

print(car1.description())
print(truck1.description())