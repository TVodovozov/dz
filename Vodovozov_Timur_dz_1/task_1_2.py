cube_list = []
count_1 = 0
count_2 = 0
for i in range(1, 1001):
    if i % 2 != 0:
        cube_list.append(i ** 3)
for number in cube_list:
    sum_number = 0
    j = number
    while j:
        sum_number += j % 10
        j = j // 10
    if sum_number % 7 == 0:
        count_1 += number
    number += 17
    sum_number = 0
    j = number
    while j:
        sum_number += j % 10
        j = j // 10
    if sum_number % 7 == 0:
        count_2 += number
print(count_1)
print(count_2)
