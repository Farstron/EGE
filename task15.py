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