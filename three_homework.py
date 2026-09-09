# Глобальная переменная стоимости поездки
TRIP_COST = 20

class TransportCard:
    def __init__(self, owner):
        # Приватные атрибуты (скрыты от прямого доступа извне)
        self.__owner = owner
        self.__balance = 0

    # Геттер для получения имени владельца
    def get_owner(self):
        return self.__owner

    # Геттер для получения баланса
    def get_balance(self):
        return self.__balance

    # Метод пополнения баланса
    def add_money(self, amount):
        if amount <= 0:
            # Вызываем ошибку, если сумма отрицательная или равна нулю
            raise ValueError("Сумма пополнения должна быть положительной")
        self.__balance += amount

    # Метод оплаты поездки
    def pay_for_trip(self):
        if self.__balance < TRIP_COST:
            # Вызываем ошибку, если денег не хватает
            raise ValueError("Недостаточно средств на карте")
        self.__balance -= TRIP_COST


print("ТЕСТИРОВАНИЕ КАРТ")

# Создаем два объекта карты
card1 = TransportCard("Иван")
card2 = TransportCard("Айсулуу")

# Пополняем карту Ивана
card1.add_money(100)

print(f"Владелец: {card1.get_owner()}") 
print(f"Баланс: {card1.get_balance()} сом")

# Иван оплачивает поездку
card1.pay_for_trip()
print(f"Баланс после поездки: {card1.get_balance()} сом") 

print("ТЕСТИРОВАНИЕ ОШИБОК (try/except)")

# 1. Попытка Айсулуу оплатить проезд с нулевым балансом
try:
    card2.pay_for_trip()
except ValueError as error:
    print(f"Ошибка Айсулуу: {error}")  

# 2. Попытка пополнить карту Ивана на отрицательную сумму
try:
    card1.add_money(-50)
except ValueError as error:
    print(f"Ошибка Ивана: {error}")