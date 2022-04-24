word = 'процент'
for i in range(1, 101):
    if i % 10 == 1 and not i == 11:
        print(str(i) + " " + word)
    elif i == 12 or i == 13 or i == 14:
        print(str(i) + " " + word + "ов")
    elif i % 10 == 2 or i % 10 == 3 or i % 10 == 4:
        print(str(i) + " " + word + "а")
    else:
        print(str(i) + " " + word + "ов")
    i += i
