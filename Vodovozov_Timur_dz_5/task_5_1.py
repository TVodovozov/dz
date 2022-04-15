def numbers_generator(num):
    for i in range(num + 1):
        if i % 2 and not 0:
            yield i


n = int(input("Введите число n: "))

for i in numbers_generator(n):
    print('next(n):', i)
