'''
Для какого наименьшего целого неотрицательного числа A выражение
(2x + 3y ≠ 60) ∨ (A ≥ x) ∨ (A ≥ y)
тождественно истинно при любых целых неотрицательных x и y?
'''

for A in range(0,1000):
    f = True
    for x in range(0,1000):
        for y in range(0,1000):
            if not((2*x + 3*y != 60) or (A >= x) or (A >= y)):
                f = False
                break
        if f == False:
            break
    if f:
        print(A)
        break
