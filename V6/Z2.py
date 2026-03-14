'''6837'''
# print('x1 x2 x3 x4 x5   f')
# for x1 in range(2):
#     for x2 in range(2):
#         for x3 in range(2):
#             for x4 in range(2):
#                 for x5 in range(2):
#                     f = ((x1 or not(x2) or not(x3) or x4 or not(x5)) and (not(x1) or not(x2) or x3 or x4 or x5) and (x1 or not(x2) or not(x3) or not(x4) or x5))
#                     print(x1,x2,x3,x4,x5, f)

from itertools import *
def f(x1,x2,x3,x4,x5):
    return (x1 or not(x2) or not(x3) or x4 or not(x5)) and (not(x1) or not(x2) or x3 or x4 or x5) and (x1 or not(x2) or not(x3) or not(x4) or x5)

for a,b,c,d,e in product([0,1], repeat=5):
    t=[(0,1,1,0,a), (0,1,1,1,0),(0,1,c,d,1),(0,0,0,1,0)]
    if len(t) == len(set(t)):
        p = ['x1','x2','x3','x4','x5']
        if [f(**dict(zip(p,r))) for r in t] == [1,b,0,e]:
            print(a,b,c,d,e)