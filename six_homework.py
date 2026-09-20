class Streamer:    
    def live(self):       
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"
    def earn(self):       
        return "Заработал 500 донатов за 2 часа"

class TikToker:    
    def live(self):        
        return "Снимаю трендовый тикток под песню месяца!"
    def viral(self):        
        return "Набрал 3 миллиона просмотров за сутки!"

class Mutant:    
    def live(self):        
        return "Я... я свечусь в темноте... это мой вайб..."
    def superpower(self):       
        return "Летаю и стреляю лазерами из глаз"

# Создаем гибридов

class GlowStreamer(Streamer, Mutant):
    # Комбинируем заработок стримера и лазеры мутанта
    def ultimate_content(self):
        return f"ШОК КОНТЕНТ! Я {self.superpower()} прямо на стриме, и благодаря этому {self.earn()}!"

class ViralCyborg(TikToker, Mutant):
    # Комбинируем вирусность тиктокера и свечение/лазеры
    def ultimate_content(self):
        return f"Тренды 2026! Я {self.superpower()} под фонк, и в итоге {self.viral()}"

class DonateMage(Streamer, TikToker):
    # Комбинируем донаты и вирусность
    def ultimate_content(self):
        return f"Гений маркетинга! Я {self.earn()} на Твиче, пока мой клип {self.viral()}!"


# Тестирование и демонстрация MRO

print("=== 1. GlowStreamer ===")
gs = GlowStreamer()
print("MRO:", [cls.__name__ for cls in GlowStreamer.mro()])
print("Вызов live():", gs.live())
# Объяснение: Сработал метод класса Streamer. 
# Почему? В MRO список идет так: [GlowStreamer, Streamer, Mutant, object]. 
# Python ищет метод слева направо. Так как Streamer указан первым в скобках (Streamer, Mutant), его метод live() перекрывает метод мутанта.
print("Ультимативная способность:", gs.ultimate_content())


print("\n=== 2. ViralCyborg ===")
vc = ViralCyborg()
print("MRO:", [cls.__name__ for cls in ViralCyborg.mro()])
print("Вызов live():", vc.live())
# Объяснение: Сработал метод класса TikToker.
# Почему? Потому что при наследовании (TikToker, Mutant) класс TikToker стоит левее, и Питон находит его метод live() первым.
print("Ультимативная способность:", vc.ultimate_content())


print("\n=== 3. DonateMage ===")
dm = DonateMage()
print("MRO:", [cls.__name__ for cls in DonateMage.mro()])
print("Вызов live():", dm.live())
# Объяснение: Снова метод от Streamer, так как в скобках (Streamer, TikToker) он стоит на первом месте.
print("Ультимативная способность:", dm.ultimate_content())