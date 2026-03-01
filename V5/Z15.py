'''8560'''
for A in range(100):
    f = True
    for x in range(200): 
        if f:
            for y in range(200):
                if f:
                    for z in range(200):
                        if not(((2*x + y) != 136) or ((z*y) < 100) or ((A**2)>= (x + y))):
                            f = False
                            break
    if f:
        print(A)
        break