d = dict()
with open('nginx_logs.txt', 'r', encoding="utf-8") as file:
    for line in file:
        el = line.split()
        ip = el[0]
        if ip not in d:
            d[ip] = 1
        else:
            d[ip] += 1
v = 0
k = '_'
for key, value in d.items():
    if value > v:
        v = value
        k = key
print(v, k)
