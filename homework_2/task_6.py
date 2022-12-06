"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

import random


def guess_num(count, number):
    try:
        answer = int(input('Введите число от 0 до 100: '))
    except ValueError:
        print('Введите число, а не строку')
    print(f'попытка номер {count}')
    if count == 10 or answer == number:
        if answer == number:
            print('Вы угадали!')
    else:
        if answer > number:
            print(f'Загаданное число меньше {answer}')
        else:
            print(f'Загаданное число больше {answer}')
        guess_num(count + 1, number)


guess_num(1, random.randint(0, 100))