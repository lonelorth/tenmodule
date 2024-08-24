from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.day = 0
        self.num_vragov = 100

    def battle_start(self):
        print(f'{self.name}, на нас напали!')

    def battle_end(self):
        print(f'{self.name} одержал победу спустя {self.day} дней(дня)!')

    def run(self):
        self.battle_start()
        while self.num_vragov > 0:
            print(f'{self.name}, сражается {self.day} день(дня), осталось {self.num_vragov} воинов.')
            self.num_vragov -= self.power
            self.day += 1
            sleep(1)
        self.battle_end()


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')