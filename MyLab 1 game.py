import random

print("Игра 'Угадай число'")
x = random.randint(0, 100)
n = int(input("Введите ваше число"))
while n != x:
    if n < x:
        print("Ваше число меньше загаданного, попробуйте еще раз")
        n = int(input("Введите ваше число"))
    else:
        print("Ваше число больше загаданного, попробуйте еще раз")
        n = int(input("Введите ваше число"))
print("Поздравляем! Вы угадали число!")

