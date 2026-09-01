class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        edu_status = "есть" if self.higher_education else "нет"
        print(f"Меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.occupation}, высшего образования {edu_status}.")


person1 = Person("Алексей", "15.04.1995", "инженер", True)
person2 = Person("Марина", "22.08.2001", "дизайнер", False)
person3 = Person("Иван", "10.11.1988", "врач", True)

print("Атрибуты экземпляров")
print(f"Объект 1: Имя: {person1.name}, ДР: {person1.birth_date}, Профессия: {person1.occupation}, В/О: {person1.higher_education}")
print(f"Объект 2: Имя: {person2.name}, ДР: {person2.birth_date}, Профессия: {person2.occupation}, В/О: {person2.higher_education}")
print(f"Объект 3: Имя: {person3.name}, ДР: {person3.birth_date}, Профессия: {person3.occupation}, В/О: {person3.higher_education}")

print("\n Вызов метода introduce")
person1.introduce()
person2.introduce()
person3.introduce()