"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв
Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.
Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""

input_string = str(input("Введите строку: "))

substring_set = set()
substring_dict = {}


def unique_substring(words):
    for i in range(len(input_string)):
        for j in range(len(input_string) - 1 if i == 0 else len(input_string), i, -1):
            substring_set.add(hash(input_string[i:j]))
            print(input_string[i:j])
            substring_dict[input_string[i:j]] = hash(input_string[i:j])
    return words


s = unique_substring(input_string)
print(f'{s} - {len(substring_set)} уникальных подстрок')
