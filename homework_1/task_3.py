"""
Задание 3.
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

companies_dict = {'Toyota': 12345,
                  'Honda': 123456,
                  'Mazda': 1234567,
                  'Subaru': 12345678,
                  'Nissan': 123456789}

# Первое решение

highest_revenue_1 = sorted(list(companies_dict.values()), reverse=True)[:3]  # O(n)
for i in highest_revenue_1:  # O(1)
    for k, v in companies_dict.items():  # O(n)
        if v == i:
            print(k + ':', v)  # O(1)

# Сложность: O(n)

print("**********************************")

# Второе решение

highest_revenue_2 = sorted(companies_dict, key=companies_dict.get, reverse=True)[:3]  # O(n*log n)
for i in highest_revenue_2:  # O(1)
    print(i + ':', companies_dict.get(i))  # O(1)

# Сложность: O(n *log n)

# Вывод: второй способ эффективнее, конечная сложность O(n *log n) меньше, чем O(n) второго алгоритма.