src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_nums = set()
temp = set()
for i in src:
    if i not in temp:
        unique_nums.add(i)
    else:
        unique_nums.discard(i)
    temp.add(i)
result = [i for i in src if i in unique_nums]
print(result)
