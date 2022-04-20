price_list = [4.8, 22.51, 9.6, 101.15, 54.34, 47.57, 35.22, 66.10, 511.53, 21.11,
              997, 0.32, 33.99, 8.2, 52.23, 93.74, 1112.77, 320.85]
comma = ', '
for i, num in enumerate(sorted(price_list)):
    price = str(f"{float(num):.2f}").split(".")
    if i == len(price_list) - 1:
        comma = "\n"
    print(f"{price[0]} руб {price[1]} коп", end=comma)
comma = ', '
copy_price_list = price_list.copy()
copy_price_list.sort(reverse=True)
for i, num in enumerate(copy_price_list):
    price = str(f"{float(num):.2f}").split(".")
    if i == len(price_list) - 1:
        comma = "\n"
    print(f"{price[0]} руб {price[1]} коп", end=comma)

print(sorted(price_list, reverse=True)[:5])
