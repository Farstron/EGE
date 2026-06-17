'''
Петя и Ваня решили поиграть. Перед ними лежат две кучи камней. Ребята ходят по очереди, 
первый ход делает Петя. За один ход игрок может убрать из любой кучи два камня или уменьшить 
количество камней в большей куче в два раза (с округлением в большую сторону).

Например, пусть в одной куче 8, а в другой 11 камней; эту позицию мы будем обозначать так: 
(8, 11). За один ход из позиции (8, 11) можно получить любую из трёх позиций: (6, 11), (8, 9), (8, 6). 
Игра завершается в тот момент, когда суммарное количество камней в кучах становится не более 33. 
Победителем считается игрок, который сделал последний ход, то есть первым получил позицию, в которой в кучах будет 33 камня или меньше. 
В начале игры в первой куче было 23 камня, во второй — S камней,  S>10.
'''

# def step(h):
#     k1, k2 = h
#     return (
#         (k1 - 2, k2),# от условия
#         (k1, k2 - 2),# от условия
#         (round(k1/2) if k1 >= k2 else k1, round(k2/2) if k2 > k1 else k2) # от условия
#     )

# def game(h, max_moves, w_s, move=0, results=None):
#     if results is None:
#         results = []
#     # если уже победа
#     if sum(h) <= w_s: # от условия оператор
#         winner = 'Петя' if move % 2 == 1 else 'Ваня'
#         results.append({
#             'status': 'win',
#             'winner': winner,
#             'move': move
#         })
#         return results

#     # если достигли лимита ходов, но победы нет
#     if move == max_moves:
#         results.append({
#             'status': 'no win',
#             'winner': None,
#             'move': move
#         })
#         return results

#     # продолжаем игру
#     for next_h in step(h):
#         game(next_h, max_moves, w_s, move + 1, results)

#     return results
# def step(h):
#     k1, k2 = h
#     return (
#         (k1 - 2, k2),
#         (k1, k2 - 2),
#         (round(k1 / 2) if k1 >= k2 else k1,
#          round(k2 / 2) if k2 > k1 else k2)
#     )

# def f(h, m, w_s):
#     if sum(h) <= w_s:
#         return m % 2 == 0
#     if m == 0:
#         return False

#     moves = [f(x, m - 1, w_s) for x in step(h)]

#     # если сейчас ход игрока, который должен добиться победы
#     if m % 2 == 1:
#         return any(moves)
#     else:
#         return all(moves)

# ans19 = []

# for s in range(10, 1000):
#     if not f((23, s), 1, 33) and f((23, s), 2, 33):
#         ans19.append(s)

# print(max(ans19))
# # 19 задание
'''
Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети.

Укажите максимальное значение S, при котором такая ситуация возможна.
'''
# f = True
# for S in range(200,10,-1): # от условия
#     if f:
#         res = game((23,S),2,33) # от условия аргументы
#         for el in res:
#             if el['status'] == 'win' and el['move'] == 2: # от условия
#                 print(S)
#                 f = False
#                 break
#     else: break

# 20
'''
Найдите минимальное и максимальное значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:

Петя не может выиграть за один ход
Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня
Найденные значения запишите в ответе в порядке возрастания.
'''
# S20 = {key:0 for key in range(10,100)}
# for S in range(10,100): # от условия
#         res = game((23,S),3,33) # от условия аргументы
#         for el in res:
#             if el['status'] == 'win' and el['move'] == 3: # от услови
#                 S20[S] += 1

# print(S20) 


# 21
'''
Найдите максимальное значение S, при котором одновременно выполняются два условия:

у Вани есть выигрышная стратегия, которая позволяет ему выиграть первым или вторым ходом при любой игре Пети
у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом
'''

# S21 = []
# for S in range(17,43): # от условия
#         res = game((23,S),4,33) # от условия аргументы
#         for el in res:
#             if (el['status'] == 'win' and el['move'] == 4) or (el['status'] == 'win' and el['move'] == 2): # от условия
#                 S21.append(S)
# print({el:S21.count(el) for el in set(S21)})
# print("______")
# S21 = []
# for S in range(200,10,-1): # от условия
#         res = game((23,S),2,33) # от условия аргументы
#         for el in res:
#             if el['status'] == 'win' and el['move'] == 2: # от условия
#                 S21.append(S)
# print(set(S21))


# def step(h): 
#     k1, k2 =h
#     return((k1 - 2,k2), (k1, k2 - 2), (round(k1/2) if k1 >= k2 else k1, round(k2/2) if k2 > k1 else k2))
# def game(h, max_moves, w_s, move = 0, results=None): 
#     if results is None:
#         results = []
#     if sum(h) <= w_s:
#         winner = 'Петя' if move % 2 == 1 else 'Ваня'
#         results.append({'status' : 'win',
#                         'winner' : winner,
#                          'move' : move})
#         return results
#     if move == max_moves:
#         results.append({'status' : 'no win',
#                         'winner' : None,
#                         'move': move})
#         return results
#     for next_h in step(h):
#         game(next_h, max_moves, w_s, move +1 , results)
#     return results

# f= True
# for S in range(200,0,-1):
#     if f:
#         res = game((23,S),2, 33)
#         for el in res:
#             if el['status'] == 'win' and el['move'] == 2:
#                 print(S)
#                 f =False
#                 break
#     else: break        

'''19,20,21'''
# def f(k, x):
#     if k >= 40:
#         return x % 2 == 0
#     if x == 0:
#         return 0
#     h = [f(k + 1, x -1) , f(k + 4, x - 1 ), f(k * 2, x - 1)]
#     return any (h) if x % 2 != 0 else all(h)

# print([k for k in range(1,40) if f(k,2)])
# print([k for k in range(1,40) if not f(k,1) and f(k,3)])
# print([k for k in range(1,40) if not f(k,2) and f(k,4)])


# def f(k, x):
#     if k <= 11:
#         return x % 2 == 0
#     if x == 0:
#         return 0
#     h = [f(k - 3, x - 1) , f(k - 7, x - 1), f(k // 3, x - 1)]
#     return any (h) if x % 2 != 0 else all(h)

# print([k for k in range(12,1000) if f(k,2)])
# print([k for k in range(12,1000) if not f(k,1) and f(k,3)])
# print([k for k in range(12,1000) if not f(k,2) and f(k,4)])


# def f(k1,k2,x):
#     if k1 + k2 >= 77:
#         return x % 2== 0
#     if x  == 0:
#         return  0
#     h = [f(k1 + 1, k2, x - 1),f(k1 * 2, k2, x - 1),f(k1, k2 + 1, x -1 ),f(k1, k2 * 2, x - 1)]
#     return any(h) if x % 2 != 0 else all(h)

# print([k for k in range(1,70) if f(7, k, 2)])
# print([k for k in range(1,70) if not f(7, k, 1) and f(7,k,3)])
# print([k for k in range(1,70) if not f(7, k, 2) and f(7, k, 4 )])


# def f (k, x ):
#     if k <= 19:
#         return x % 2 == 0
#     if x == 0:
#         return 0
#     h = ([f(k-5, x - 1)])
#     if k % 2 == 0: 
#         h.append(f(k// 2, x -1))
#     if k % 3 == 0: 
#         h.append(f(k// 3, x - 1))
#     if k % 2 != 0 and k % 3!= 0: 
#         h.append(f(k + 1, x - 1))
#     return any(h) if x % 2 != 0 else all(h)

# print([k for k in range(20, 1000) if f(k,2)])
# print([k for k in range(20, 1000) if not f(k,1) and f(k, 3)])
# print([k for k in range(20, 1000) if not f(k,2) and f(k, 4)])

# def f(k, x):
#     if k >= 59: 
#         return x % 2 == 0
#     if x == 0:
#         return 0
#     h = ([f(k + 1, x - 1), f(k + 3, x - 1), f(k * 4, x - 1)])
#     return any(h) if x % 2 != 0 else all(h)

# print([k for k in range(1, 59) if f(k,2)])
# print([k for k in range(1, 59) if not f(k,1) and f (k,3)])
# print([k for k in range(1, 59) if not f(k,2) and f (k,4)])

# def f(k1, k2, x):
#     if k1 + k2 >= 123:
#         return x % 2 == 0
#     if x == 0:
#         return 0
#     h = [f(k1 + 1, k2, x - 1), f(k1 * 2, k2, x - 1 ),f(k1, k2 + 1 , x - 1),f(k1, k2 * 2, x - 1)]
#     return any(h) if x % 2 != 0 else all(h)

# print([k for k in range(1, 110) if f(13,k,2)])
# print([k for k in range(1, 110) if not f(13,k,1) and f(13,k,3)])
# print([k for k in range(1, 110) if not f(13,k,2) and f(13,k,4)])


# def f(k1,k2,x):
#     if k1 + k2 <=  147:
#         return x % 2 == 0
#     if x == 0:
#         return 0
#     h = [f(k1 - 1 , k2, x - 1), f(k1 //2, k2, x - 1), f(k1, k2 - 1, x - 1), f(k1, k2//2, x - 1)]
#     return any(h) if x % 2 != 0 else all(h)
# print([k for k in range(135,301) if f(13,k,2)])
# print([k for k in range(135,301) if not f(13,k,1) and f(13,k,3)])
# print([k for k in range(135,301) if not f(13,k,2) and f(13,k,4)])


def f(k1,k2,x):
    if k1 + k2 >= 259:
        return x % 2 == 0
    if x == 0:
        return 0
    h =[f(k1 + 1,k2,x-1), f(k1 * 2, k2 , x - 1), f(k1, k2 + 1, x - 1), f(k1, k2 * 2, x - 1)]
    return any(h) if x % 2 != 0 else all(h)
print([k for k in range(1,242) if f(17,k,2)])
print([k for k in range(1,242) if not f(17,k,1) and f(17,k,3)])
print([k for k in range(1,242) if not f(17,k,2) and f(17,k,4)])
