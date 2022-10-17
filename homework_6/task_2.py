"""
Задание 2.
Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.
Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile
from memory_profiler import memory_usage


def memory_dec(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_delta = m2[0] - m1[0]
        print(f"Выполнение {func.__name__} использовало {mem_delta} Mib")
        return res

    return wrapper


def prove_equality(num, total=0):
    if num < 1:
        return total
    else:
        total += num
    return prove_equality(num - 1, total)


@profile
@memory_dec
def main(num):
    return num


my_num = 100

if __name__ == '__main__':
    print(main(prove_equality(my_num)))
    print(prove_equality(my_num) == my_num * (my_num + 1) / 2)

"""
При каждом вызове рекурсии вызывается профайлер, в результате мы не видим общего значения потребления памяти т.к. 
профилируется каждый ее запуск.
Чтобы видеть реальный результат нужно делать декоратор или вызывать из другой функции
"""
