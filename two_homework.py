class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        edu_status = "есть" if self.higher_education else "нет"
        print(f"Привет, меня зовут {self.name}, я родился {self.birth_date}, по профессии {self.occupation}, высшего образования {edu_status}.")


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я твой одногруппник из группы {self.group_name}, я родился {self.birth_date}, работаю {self.occupation}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я твой друг, люблю {self.hobby}, я родился {self.birth_date}, работаю {self.occupation}.")


#ДОП ЗАДАНИЕ 2 (Многоуровневое наследование)

class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, shared_memory):
        # Вызываем __init__ у класса Friend, который в свою очередь вызовет __init__ у Person
        super().__init__(name, birth_date, occupation, higher_education, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        # Сначала отрабатывает introduce() из класса Friend
        super().introduce()
        # А затем мы просто допечатываем уникальную строку
        print(f"И самое главное — у нас есть общее воспоминание: {self.shared_memory}")


#ДОП ЗАДАНИЕ 1 (Полиморфизм)

print("--- ЗАПУСК ЦИКЛА ПО СПИСКУ ОБЪЕКТОВ ---")

# Создаем по одному объекту каждого класса
person_obj = Person("Азамат", "10.05.1990", "инженер", True)
classmate_obj = Classmate("Бектур", "05.12.2000", "backend-разработчик", False, "Backend-24")
friend_obj = Friend("Алмаз", "20.10.1999", "архитектор", True, "играть в русский бильярд")
best_friend_obj = BestFriend("Нурбек", "15.06.1998", "менеджер", True, "отдых на природе", "поездка на горячие источники в Иссык-Ату")

# Помещаем всех в один список
people_list = [person_obj, classmate_obj, friend_obj, best_friend_obj]

# Проходимся циклом и заставляем каждого представиться
for person in people_list:
    person.introduce()
    print("-" * 40) # Просто разделитель для красоты в консоли