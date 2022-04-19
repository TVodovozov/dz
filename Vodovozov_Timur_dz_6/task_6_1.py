resulte = []
with open('nginx_logs.txt', 'r', encoding="utf-8") as file:
    for line in file:
        el = line.split()
        resulte.append((el[0], el[5].strip('"'), el[6]))
print(resulte)
