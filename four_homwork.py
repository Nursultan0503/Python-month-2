class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

    # Статический метод - не принимает self, работает просто как функция
    @staticmethod
    def validate_phone_number(phone_number):
        # Проверяем, что в номере ровно 10 символов и все они - цифры
        return len(phone_number) == 10 and phone_number.isdigit()


class ContactList:
    # Переменная уровня класса - общая для всех
    all_contacts = []

    # Метод класса - работает с самим классом (cls), а не с конкретным объектом (self)
    @classmethod
    def add_contact(cls, name, phone_number):
        # 1. Проверяем номер с помощью статического метода из класса Contact
        if not Contact.validate_phone_number(phone_number):
            # Если вернулось False, вызываем ошибку (как требуется в задании)
            raise ValueError(f"Ошибка: Номер '{phone_number}' некорректен. Должно быть ровно 10 цифр.")
        
        # 2. Если номер правильный - создаем объект контакта
        new_contact = Contact(name, phone_number)
        
        # 3. Добавляем объект в общий список класса
        cls.all_contacts.append(new_contact)


# --- ПРОВЕРКА РАБОТЫ (как в примере) ---

print(f"Список контактов до добавления: {ContactList.all_contacts}")

# Добавляем валидные контакты
ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

print("\nМои контакты:")
# Проходимся циклом по списку объектов
for contact in ContactList.all_contacts:
    print(f"{contact.name} - {contact.phone_number}")

print("\n--- Проверка ошибки ---")
# Пытаемся добавить контакт с неверным номером (обрабатываем ошибку через try/except для красоты вывода)
try:
    ContactList.add_contact("John Doe", "5551234") 
except ValueError as e:
    print(e)