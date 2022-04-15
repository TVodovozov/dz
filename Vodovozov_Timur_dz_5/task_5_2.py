n = int(input("Введите число n: "))
numbers_generator = [i for i in range(n + 1) if i % 2]
print('next(n):', numbers_generator)
