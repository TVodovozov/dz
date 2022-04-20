weather_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
length_of_list: int = len(weather_list)
for _ in range(length_of_list):
    elem = weather_list.pop(0)
    if elem.isdigit() and elem.isalnum():
        weather_list.append(f'"{int(elem):02d}"')
    elif elem[0] == "+" and elem[1].isdigit():
        weather_list.append(f'"+{int(elem):02d}"')
    else:
        weather_list.append(elem)
print(' '.join(weather_list))
