name = "Иван", "Мария", "Петр", "Илья", "Сергей"
name_letter = []
capital_letter = {}


def thesaurus(name):
    def thesaurus_capital_letters(name):
        return name.startswith(list_names)

    for i in name:
        name_letter.append(name[name.index(i)][:1])
        list_names = name[name.index(i)][:1]
        name_staff = list(filter(thesaurus_capital_letters, name))
        capital_letter[list_names] = name_staff
    return capital_letter


print(thesaurus(name))
