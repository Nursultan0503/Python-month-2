import sqlite3

# Название файла базы данных (он будет проигнорирован гитом благодаря .gitignore)
DB_NAME = "library.db"

def create_table():
    # Подключаемся к БД (используем менеджер контекста with, чтобы соединение закрывалось само)
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                author TEXT,
                publication_year INTEGER,
                genre TEXT,
                number_of_pages INTEGER,
                number_of_copies INTEGER
            )
        ''')
        print("Таблица 'books' успешно создана или уже существует.")

def insert_books(name, author, publication_year, genre, number_of_pages, number_of_copies):
    with sqlite3.connect(DB_NAME) as conn:
        # Используем параметризованный запрос (?) для защиты от SQL-инъекций
        conn.execute('''
            INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, author, publication_year, genre, number_of_pages, number_of_copies))
        print(f"Книга '{name}' успешно добавлена.")

# Блок запуска
if __name__ == "__main__":
    # 1. Сначала создаем таблицу
    create_table()
    
    # 2. Вызываем функцию 10 раз для добавления книг
    print("\nНачинаем добавление книг:")
    insert_books("1984", "Джордж Оруэлл", 1949, "Антиутопия", 328, 5)
    insert_books("Мастер и Маргарита", "Михаил Булгаков", 1967, "Роман", 480, 12)
    insert_books("Преступление и наказание", "Федор Достоевский", 1866, "Классика", 672, 8)
    insert_books("Гарри Поттер и философский камень", "Дж. К. Роулинг", 1997, "Фэнтези", 332, 20)
    insert_books("Властелин колец", "Дж. Р. Р. Толкин", 1954, "Фэнтези", 1178, 4)
    insert_books("Совершенный код", "Стив Макконнелл", 2004, "Программирование", 914, 3)
    insert_books("Грокаем алгоритмы", "Адитья Бхаргава", 2016, "Обучение", 290, 7)
    insert_books("Дюна", "Фрэнк Герберт", 1965, "Научная фантастика", 704, 15)
    insert_books("Гордость и предубеждение", "Джейн Остин", 1813, "Роман", 432, 6)
    insert_books("Основы Python", "Аллен Дауни", 2015, "Программирование", 300, 10)