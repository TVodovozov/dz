duration = int(input('Введите число в секундах: '))
days = (duration // 86400)
hours = (duration - days * 86400) // 3600
minutes = (duration // 60) % 60
seconds = duration % 60
if duration <= 59:
    print(duration, 'сек')
elif 60 <= duration < 3600:
    print(minutes, 'мин', seconds, 'сек')
elif 3600 <= duration < 86400:
    print(hours, 'ч', minutes, 'мин', seconds, 'сек')
else:
    print(days, 'д', hours, 'ч', minutes, 'мин', seconds, 'сек')
