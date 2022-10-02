def my_school(lsp_1, lsp_2):
    if len(lsp_1) - len(lsp_2) > 0:
        for i in range(len(lsp_1)):
            lsp_2.append(None)
    for tutors, klasses in zip(lsp_1, lsp_2):
        yield tutors, klasses


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Ольга']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

m = my_school(tutors, klasses)
for el in m:
    print(el)
print(type(m))
