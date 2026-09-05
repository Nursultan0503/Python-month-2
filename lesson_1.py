class Car:
    # __init__ — конструктор: Python вызывает его автоматически при Car(...)
    # self — конкретный создаваемый объект
    def __init__(self, model, color):
        # self.model и self.color — атрибуты объекта
        self.model = model
        self.color = color

    def drive_to(self, destination):
        print(f"Машина цвета '{self.color}' поехала в {destination}")

    def change_color(self, new_color):
        self.color = new_color


# класс для игрового персонажа, добавить любые свойства на усмотрение
# и создать 1-2 объекта
class GameCharacter:
    # pass оставляет класс пустым; свойства и методы нужно добавить самостоятельно
    pass

hero1 = GameCharacter()
hero2 = GameCharacter()

# https://github.com/
# создание объекта путем "вызова" класса
car1 = Car("Kia", "серебристый") # создание объекта вызывает __init__ автоматически
car2 = Car("BMW", "черный")
# Без специального метода Python выводит служебное представление объекта
print(car1)
print(car2)
print(car1.model, car1.color) # обращение к атрибутам/свойствам объекта
print(car2.model, car2.color)
car2.change_color("белый")
print(car2.model, car2.color)
print(type(car1)) # тип объекта - его класс
print(type("Kia"), type(1223))
car1.drive_to("Кант")
# Атрибут объекта можно изменить после его создания
car1.model = "Subaru"
print(car1.model)
car2.fined = True # можно, но не стоит так делать
# Атрибут fined добавляется только объекту car2, а не всем объектам Car
print(car2.fined)
# print(car1.fined) # возникнет AttributeError: у car1 нет такого атрибута
