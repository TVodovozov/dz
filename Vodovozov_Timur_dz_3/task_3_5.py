import random


def get_jokes(n, i):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    while i <= n:
        thing = random.choice(nouns)
        nouns.remove(thing)
        time = random.choice(adverbs)
        adverbs.remove(time)
        adjective = random.choice(adjectives)
        adjectives.remove(adjective)
        jokes.append(f'{thing} {time} {adjective}')
        i += 1
    return print(jokes)


get_jokes(int(input('Введите n шуток: ')), 1)
