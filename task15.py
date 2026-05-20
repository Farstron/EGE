'''
Для какого наименьшего целого неотрицательного числа A выражение
(2x + 3y ≠ 60) ∨ (A ≥ x) ∨ (A ≥ y)
тождественно истинно при любых целых неотрицательных x и y?
'''

# for A in range(0,1000):
#     f = True
#     for x in range(0,1000):
#         for y in range(0,1000):
#             if not((2*x + 3*y != 60) or (A >= x) or (A >= y)):
#                 f = False
#                 break
#         if f == False:
#             break
#     if f:
#         print(A)
#         break

'''
Обозначим через m&n поразрядную конъюнкцию неотрицательных целых чисел m и n. Например, 14&5  =  11102&01012  =  01002  =  4. 
Для какого наименьшего неотрицательного целого числа А формула
(x&5160 > 0 ∨ x&3650 > 0) → (x&9545 = 0 → x&A > 0)
тождественно истинна (т. е. принимает значение 1 при любом неотрицательном целом значении переменной х)?
'''

# for A in range(0,10000):
#     f = True
#     for x in range(0,10000):
#         if not(((x&5160 > 0) or (x&3650 > 0)) <= ((x&9545 == 0) <= (x&A > 0))):
#             f = False
"""
Для какого наименьшего целого неотрицательного числа А выражение
(x + 2y < A) ∨ (y > x) ∨ (x > 30)
тождественно истинно, то есть принимает значение 1 при любых целых неотрицательных x и y?
"""

# for A in range(0,1000):
#     f = True
#     for x in range(0,1000):
#         for y in range(0,1000):
#             if not ((x + 2*y < A) or (y > x) or (x > 30)):
#                 f = False
#                 break
#         if f == False:
#             break
#     if f:
#         print(A)
#         break

'''
Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
Для какого наибольшего натурального числа А формула
ДЕЛ(90, A) ∧ (¬ДЕЛ(x, А) → (ДЕЛ(x, 15) → ¬ДЕЛ(x, 20)))
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?
'''
# def DEL(n,m):
#     if n % m == 0:
#         return True
#     return False

# for A in range(1000,0,-1):
#     f = True
#     for x in range(0,1000):
#         if not(DEL(90, A) and ((not(DEL(x, A))) <= (DEL(x, 15) <= (not DEL(x, 20))))):
#             f = False
#             break
#     if f:
#         print(A)
#         break

'''
Для какого наименьшего целого неотрицательного числа A выражение
(3x + 4y ≠ 60) ∨ ((A ≥ x) ∧ (A ≥ y))
тождественно истинно при любых целых неотрицательных x и y?
'''

# for A in range(0,1000):
#     f = True
#     for x in range(0,1000):
#         for y in range(0,1000):
#             if not((3*x + 4*y != 60)or ((A >= x) and (A >= y))):
#                    f = False
#                    break 
#         if f == False:
#             break
#     if f:
#         print(A)
#         break

'''
Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
Укажите наименьшее целое значение A, для которого формула
(ДЕЛ(72, x) → ¬ДЕЛ(90, x)) ∨ (A − x > 80)
тождественно истинна при любом натуральном значении переменной x.
'''

# def DEL(n,m):
#     if n % m == 0:
#         return True
#     return False

# for A in range(1000):
#     f = True
#     for x in range(1,1000):
#         if not(((DEL(72,x)) <= (not (DEL(90,x)))) or (A - x > 80)):
#             f = False 
#             break
#     if f:
#         print(A)
#         break


'''
Обозначим через m&n поразрядную конъюнкцию неотрицательных целых чисел m и n.
Например, 14&5  =  11102&01012  =  01002  =  4.
Для какого наименьшего неотрицательного целого числа А формула
x&25 ≠ 0 → (x&9 = 0 → x&А ≠ 0)
тождественно истинна (т. е. принимает значение 1 при любом неотрицательном целом значении переменной х)?
'''

# for A in range(10000):
#     f = True
#     for x in range(10000):
#         if not ((x&25 != 0) <= ((x&9 == 0) <= (x&A != 0))):
#             f = False
#             break
#     if f:
#         print(A)
#         break


'''
Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
Для какого наибольшего натурального числа А формула
ДЕЛ(120, A) ∧ (ДЕЛ(x, 36) → (¬ДЕЛ(x, А) → ¬ДЕЛ(x, 45)))
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?
'''

# def DEL(n,m):
#     if n % m == 0:
#         return True
#     return False

# for A in range(1000, 0, -1):
#     f = True
#     for x in range(1000):
#         if not (DEL(120, A) and (DEL(x, 36) <= ((not DEL(x, A)) <= (not DEL(x, 45))))):
#             f = False
#             break
#     if f:
#         print(A)
#         break


# for A in range(1000, 0, -1):
#     f = True
#     for x in range(1000):
#         if not(DEL(120, A) and (DEL(x, 36) <= ((not DEL(x, A)) <= (not DEL(x, 45))))):
#             f = False
#             break
#     if f:
#         print(A)
#         break

# for A in range(100):
#     f = True
#     for x in range(100):
#         if f:
#             for y in range(100):
#                 if ((-(x-2)**2 + 3 < y) or ((x-1)**2 +y**2 < 7) or (5*x + A > y)):
#                     f = False
#                     break
#         if f:
#             print(A)
#             break

<<<<<<< HEAD
# for A in range(1000):
#     f = True
#     for x in range(1000):
#         if f:
#             for y in range(1000):
#                 if not((3*y -x > 12) or (2*x + 6*y >= 72) or (x > 24) or (x* y < A)):
#                     f = False
#                     break
#     if f: 
#         print(A)
#         break

def Del(n,m):
    if n % m == 0:
        return True
    return False

res = []
for A in range(1,10000):
    f = True
    for x in range(0,1000000):
        if not((not Del(x,A)) <= (not (Del(x,48) and Del(x, 35)))):
            f = False
            break
    if f:
        res.append(A)
print(max(res)) 


=======
>>>>>>> fd9ef4c91ec4c8d4ccc1e7ae3b7bdbef174554d1
