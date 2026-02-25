'''1424'''
def Tok(num,k): 
    alf = {0:'0', 1:'1', 2:'2', 3:'3'}
    res =''
    while num != 0:
        res = alf[num % k] + res
        num//=k
    return res

for N in range(1000):
    R = Tok(N,2)
    if N % 2 == 0:
        R = R + '01'
    else:
        R = R + '10'
    R = int(R,2)
    if R > 281:
        print(N)
        break 