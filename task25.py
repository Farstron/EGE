#https://education.yandex.ru/ege/inf/task/a41df56e-cc5a-4be7-9bc7-66218073e61f
D = []
for el in range(1,10001):
    el = int(str(el) + '14')
    f = True
    for k in D:
        if el % k == 0:
            f = False
            break
    if f: 
        D.append(el)
res = {}
for num in range(800_000, 2_000_000):
    if len(res) == 5:
        break
    for k in D:
        if num % k == 0 and num != k:
            res[num] = k
            break
print(res)