# A. Вычесть 1
# B. Найти целую часть от деления на 3
# C. Найти целую часть от деления на 4
# Программа для исполнителя — это последовательность команд.
# Сколько программ преобразуют число 2025 в число 25, при этом их траектория вычислений содержит число 250, но не содержит 42?

# import sys
# sys.setrecursionlimit(10**6)

# def f(start, stop, path = ''):
#     if start < stop or start == 42:
#         return 0
#     if start == stop:
#         return 1
#     return f(start - 1, stop, path + 'A') + f(start // 3, stop, path + 'B') + f(start // 4, stop, path + 'C')

# print(f(2025, 250) * f(250, 25))

# A. Вычесть 2.
# B. Найти целую часть от деления на 2.
# Программа для исполнителя — это последовательность команд.
# Сколько существует программ, для которых при исходном числе 31 результатом является число 2?

# import sys 
# sys.setrecursionlimit(10**6)

# def f(start, stop, path = ''):
#     if start < stop: 
#         return 0
#     if start == stop:
#         return 1
#     return f(start - 2, stop, path + 'A')  + f(start // 2, stop , path + 'B')

# print(f(31, 2))


# У исполнителя есть три команды, которые обозначены латинскими буквами:

# A. Прибавить 2
# B. Прибавить 3
# C. Возвести в квадрат

# Программа для исполнителя — это последовательность команд.

# Сколько существует программ, для которых при исходном числе 2 результат — число 42, при этом траектория вычислений содержит число 25 и не содержит 16?

# import sys
# sys.setrecursionlimit(10**6)

# def f(start, stop, path = ''):
#     if start > stop or start == 16:
#         return 0
#     if start == stop:
#         return 1
#     return f(start + 2, stop, path + 'A') + f(start + 3, stop, path + 'B') + f(start**2, stop, path + 'C')

# print(f(2,25) * f(25,42))

# Прибавить 3.
# Сделать нечётное.
# Следующее, кратное 3.
# Команда 1 увеличивает число на экране на 3, команда 2 получает число вида 2*х+1, команда 3 получает число, кратное 3, большее текущего.

# Программа для исполнителя — это последовательность команд.

# Сколько программ существует таких, что при исходном числе 5 будет получено число 89, при этом траектория вычислений исполнителя пройдет через число 23 и не пройдет через число 50?

# import sys
# sys.setrecursionlimit(10**6)

# def f(start, stop, path = ''):
#     if start > stop or start == 50:
#         return 0
#     if start == stop:
#         return 1
#     return f(start + 3, stop, path + 'A') + f(2*start + 1, stop, path + 'B') + f((start// 3 + 1)*3, stop, path + 'C')

# print(f(5,23) * f(23,89))


# A. Прибавить 1
# B. Прибавить 2
# С. Прибавить 4
# D. Прибавить 8

# Программа исполнителя — это последовательность команд.

# Сколько существует программ, для которых при исходном числе 16 результатом является число 48, если никакую из команд нельзя повторять дважды подряд?

# import sys
# sys.setrecursionlimit(10**6)

# def f(start, stop, path = ''):
#     if start > stop or 'AA' in path or 'BB' in path or 'CC' in path or 'DD' in path:
#         return 0
#     if start == stop:
#         return 1
#     return f(start + 1, stop, path + 'A') + f(start + 2, stop, path + 'B') + f(start + 4, stop, path + 'C') + f(start + 8, stop, path + 'D')

# print(f(16,48))



# A. Вычесть 5
# B. Сделать кратным трём
# C. Поделить на 3

# Команда A уменьшает число на экране на 5.
# Команда B может быть применена только к числам, не кратным трём, и уменьшает число на экране так, чтобы получилось ближайшее к исходному кратное трём число.
# Команда C может быть применена только к числам, кратным трём, и уменьшает число на экране в три раза.

# Программа для исполнителя — это последовательность команд.

# Сколько программ преобразуют число 103 в число 24, и при этом их траектория вычислений содержит число 73?

# import sys
# sys.setrecursionlimit(10**6)

# def f(start, stop, path = ''):
#     if start < stop:
#         return 0
#     if start == stop: 
#         return 1
#     if start % 3 != 0:
#         return f(start - 5, stop, path + 'A') + f((round(start/3) - 1 )* 3, stop, path + 'B')
#     return f(start - 5, stop, path + 'A') + f(start // 3, stop, path + 'C')
# print(f(103,73) * f(73,24))


def f(x,y):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 1, y) + f(x *2, y)
print(f(3,6)* f(6,12) * f(12,16))


def f(x,y):
    if x > y or x == 25:
        return 0
    if x == y:
        return 1
    if x < y:
        return f(x + 3, y) + f(x * 2, y) + f(x * 5, y)
print(f(5,115))

















