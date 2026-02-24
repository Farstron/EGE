'''19552'''
def Tok(num,k): 
    alf = {0:'0', 1:'1', 2:'2', 3:'3'}
    res = ''
    while num != 0: 
        res = alf[num % k] + res
        num //= k 
    return res

for N in range(1000):
    R = Tok(N,2)
    if len(R) < 2:
        continue
    if N % 2 == 0: 
        R = R + '100'
    else: 
        R = R + '011'
    r = int(R,2)
    if r > 300:
        print(N)
        break

    
