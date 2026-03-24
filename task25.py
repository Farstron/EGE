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
# res = {}
# for n in range(10):
#     for n1 in range(-1,10):
#         for n2 in range(-1,10):
#             for n3 in range(-1,10):
#                 num = int(f'1{n}2157{n1 if n1 > -1 else ''}{n2 if n2 > -1 else ''}{n3 if n3 > -1 else ''}4')
#                 if num % 2024 == 0:
#                     res[num] = num//2024

# for el in sorted(res):
#     print(f'{el}')
# print("________", 1621570104 % 2024)
# for el in sorted(res):
#     print(f'{res[el]}')

# https://education.yandex.ru/ege/inf/task/933e19be-0afe-4b69-92ac-c92b5d4c11e4
# 53*23*0
# 53XXXXX230
# res = {}

# for n1 in range(-1,10):
#     for n2 in range(-1,10):
#         for n3 in range(-1,10):
#             for n4 in range(-1,10):
#                 for n5 in range(-1,10):
#                     num1 = int(f'53{n1 if n1 > -1 else ''}{n2 if n2 > -1 else ''}{n3 if n3 > -1 else ''}{n4 if n4 > -1 else ''}{n5 if n5 > -1 else ''}230')
#                     if num1 % 2026 == 0:
#                         res[num1] = num1//2026
#                     num2 = int(f'53{n1 if n1 > -1 else ''}{n2 if n2 > -1 else ''}{n3 if n3 > -1 else ''}{n4 if n4 > -1 else ''}23{n5 if n5 > -1 else ''}0')
#                     if num2 % 2026 == 0:
#                         res[num2] = num2//2026
#                     num3 = int(f'53{n1 if n1 > -1 else ''}{n2 if n2 > -1 else ''}{n3 if n3 > -1 else ''}23{n4 if n4 > -1 else ''}{n5 if n5 > -1 else ''}0')
#                     if num3 % 2026 == 0:
#                         res[num3] = num3//2026
#                     num4 = int(f'53{n1 if n1 > -1 else ''}{n2 if n2 > -1 else ''}23{n3 if n3 > -1 else ''}{n4 if n4 > -1 else ''}{n5 if n5 > -1 else ''}0')
#                     if num4 % 2026 == 0:
#                         res[num4] = num4//2026
#                     num5 = int(f'53{n1 if n1 > -1 else ''}23{n2 if n2 > -1 else ''}{n3 if n3 > -1 else ''}{n4 if n4 > -1 else ''}{n5 if n5 > -1 else ''}0')
#                     if num5 % 2026 == 0:
#                         res[num5] = num5//2026
#                     num6 = int(f'5323{n1 if n1 > -1 else ''}{n2 if n2 > -1 else ''}{n3 if n3 > -1 else ''}{n4 if n4 > -1 else ''}{n5 if n5 > -1 else ''}0')
#                     if num6 % 2026 == 0:
#                         res[num6] = num6//2026


# for i in range(6):
#     print(f'{sorted(res, reverse=True)[i]}')
# print("________")
# for i in range(5):
#     print(f'{res[sorted(res, reverse=True)[i]]}')



# https://education.yandex.ru/ege/inf/task/83b21e05-822c-44b1-b785-f14418c83449
res ={}
L = list(range(200000000,-1,-1))
for i  in range(len(L)):
    if len(res) == 5:
        break
for n in range(10):
    for n1 in range(-1,10):
        for n2 in range(-1,10):
            num = int(f'{n}2{n1 if n1> -1 else ''}4{n2 if n2 > -1 else ''}0')
            num1 = int(f'1{n1 if n1> -1 else ''}7{n2 if n2 > -1 else ''}')
            if num == res and num1 != res and res % 42 == 0:
                print(res)