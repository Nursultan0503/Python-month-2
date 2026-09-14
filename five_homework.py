# Импортируем инструменты для создания абстрактных классов
from abc import ABC, abstractmethod

# 1. Создаем абстрактный базовый класс
class File(ABC):
    
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def get_file_info(self):
        pass

# 2. Классы-наследники
class TextFile(File):
    def open(self):
        print("Открытие текстового файла: 'Привет, мир!'")

    def get_file_info(self):
        print("Информация: Текстовый файл (.txt), размер 15 КБ")

class ImageFile(File):
    def open(self):
        print("Открытие изображения:")
        print("  /\\_/\\")
        print(" ( o.o )")
        print("  > ^ <")

    def get_file_info(self):
        print("Информация: Изображение (.png), разрешение 1920x1080")

class AudioFile(File):
    def open(self):
        print("Воспроизведение аудио: ♫ ♪ ♫ (Играет музыка)")

    def get_file_info(self):
        print("Информация: Аудиофайл (.mp3), длительность 3:45")

class VideoFile(File):
    def open(self):
        print("Воспроизведение видео: Запуск видеоплеера...")

    def get_file_info(self):
        print("Информация: Видеофайл (.mp4), качество 4K, длительность 1:20:00")

# --- Основная часть программы (Демонстрация полиморфизма) ---
print("=== Запуск всех файлов ===\n")

# Список файлов, включая дополнительный VideoFile
files = [
    TextFile(),
    ImageFile(),
    AudioFile(),
    VideoFile() 
]

# В цикле обращаемся к каждому объекту через единый интерфейс
for file in files:
    file.open()
    file.get_file_info()
    print("-" * 25)


# ОТВЕТЫ НА ВОПРОСЫ ИЗ ЗАДАНИЯ (Закомментировано, чтобы не ломать код)

# Вопрос 1: Попробуйте создать объект File. Что произойдёт?
# my_file = File() 
# Ответ: Произойдет ОШИБКА TypeError (Can't instantiate abstract class File with abstract methods get_file_info, open). 
# Python скажет, что нельзя создать объект абстрактного класса (чертежа).

# Вопрос 2: Создайте класс ArchiveFile, но реализуйте только open(). Почему Python не позволяет это сделать?
# class ArchiveFile(File):
#     def open(self):
#         print("Распаковка архива...")
#
# archive = ArchiveFile()
# Ответ: Произойдет ОШИБКА TypeError (Can't instantiate abstract class ArchiveFile with abstract method get_file_info).
# Python не позволит создать объект, потому что ArchiveFile унаследовал статус "абстрактного". 
# Чтобы класс перестал быть абстрактным, он ОБЯЗАН реализовать ВСЕ абстрактные методы родителя (в данном случае мы забыли про get_file_info).