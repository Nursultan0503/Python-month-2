import sqlite3

DB_NAME = "library.db"

def create_table():
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
        print("Таблица 'books' готова к работе.")

def insert_books(name, author, publication_year, genre, number_of_pages, number_of_copies):
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, author, publication_year, genre, number_of_pages, number_of_copies))
        print(f"Книга '{name}' добавлена.")


# НОВЫЕ ФУНКЦИИ (ДЗ №8)


def get_books_by_author(author):
    with sqlite3.connect(DB_NAME) as conn:
        # SELECT * означает "выбрать все колонки"
        cursor = conn.execute('SELECT * FROM books WHERE author = ?', (author,))
        # fetchall() возвращает список кортежей со всеми найденными записями
        books = cursor.fetchall()
        
        print(f"\n--- Результаты поиска для автора '{author}' ---")
        if books:
            for book in books:
                # book - это кортеж: (id, name, author, year, genre, pages, copies)
                print(book)
        else:
            print("Книги этого автора не найдены.")
            
        return books

def delete_book_by_id(book_id):
    with sqlite3.connect(DB_NAME) as conn:
        # DELETE FROM удаляет строку, где id совпадает с переданным
        conn.execute('DELETE FROM books WHERE id = ?', (book_id,))
        print(f"\n[Успешно] Книга с ID {book_id} была удалена из базы данных.")


# БЛОК ЗАПУСКА

if __name__ == "__main__":
    # 1. Создаем таблицу
    create_table()

    # одни и те же 10 книг при перезапуске скрипта!
    """
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
    """

    # 2. Проверяем выборку по автору
    get_books_by_author("Дж. К. Роулинг")
    
    # 3. Проверяем удаление по ID (например, удалим книгу с ID 1 - "1984")
    delete_book_by_id(1)