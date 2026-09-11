class Animal:
    def __init__(self, name, age):
        # Приватные атрибуты
        self.__name = name
        self.__age = age

    # Геттеры (для получения данных)
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    # Сеттеры (для изменения данных)
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError("Возраст не может быть отрицательным!")

    # Базовый метод
    def make_sound(self):
        print("Животное издает какой-то звук")


# Класс-наследник Dog
class Dog(Animal):
    # Переопределяем метод (Полиморфизм)
    def make_sound(self):
        # Используем get_name(), так как напрямую к __name обратиться нельзя
        print(f"Собака {self.get_name()} говорит: Гав-гав!")


# Класс-наследник Cat
class Cat(Animal):
    # Переопределяем метод (Полиморфизм)
    def make_sound(self):
        print(f"Кошка {self.get_name()} говорит: Мяу-мяу!")


print("--- Демонстрация полиморфизма ---")
dog = Dog("Рекс", 5)
kitty = Cat("Мурка", 1)

# Оба объекта реагируют на одну и ту же команду по-разному
dog.make_sound()
kitty.make_sound()


print("\n--- Демонстрация сеттеров и геттеров ---")
print(f"Изначальный возраст кошки: {kitty.get_age()}")

# Изменяем возраст через сеттер (как в условии задачи)
kitty.set_age(2)

print(f"Новый возраст кошки: {kitty.get_age()}")

# Меняем имя собаке
dog.set_name("Супер-Рекс")
dog.make_sound()