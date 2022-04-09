def num_translate(word):
    translate_dict = {"zero": "ноль", 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четрые', 'five': "пять",
                      'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if word.istitle() and translate_dict.get(word.lower()):
        return translate_dict.get(word.lower()).title()
    else:
        return translate_dict.get(word)


print(num_translate(input('Введите слово: ')))
