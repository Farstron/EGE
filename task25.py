#https://education.yandex.ru/ege/inf/task/a41df56e-cc5a-4be7-9bc7-66218073e61f
# D = []
# for el in range(1,10001):
#     el = int(str(el) + '14')
#     f = True
#     for k in D:
#         if el % k == 0:
#             f = False
#             break
#     if f: 
#         D.append(el)
# res = {}
# for num in range(800_000, 2_000_000):
#     if len(res) == 5:
#         break
#     for k in D:
#         if num % k == 0 and num != k:
#             res[num] = k
#             break
# print(res)


#https://education.yandex.ru/ege/inf/task/3f5102d3-428f-4585-ae99-6b6969e890cd
# res = {}
# L = list(range(33333,55_556))
# for i in range(len(L)):
#     if len(res) == 10:
#         break
#     if int(str(L[i])[0]) % 2 == 1 and int(str(L[i])[1]) % 2 == 1:
#         if L[i] % 7 == 0 and L[i] % 11 == 0 and L[i] % 13 == 0:
#             print(L[i])
#             res[i+1] = L[i]
# print(res)


#https://education.yandex.ru/ege/inf/task/c80fcaf5-ea0b-4d7b-83f6-69ef3c0a1471
# 1?2157*4
# 1021574 10^6
# 10215704 10^7
# 102157004 10^8
# 1021570004 10^9
res = {}
for n1 in range(10):
    for n2 in range(-1,1000):
        if n2 > -1:
            num = int(f'1{n1}2157{n2}4')
        else:
            num = int(f'1{n1}21574')
        if num % 2024 == 0:
            res[num] = num//2024
print({el:res[el] for el in sorted(res)})