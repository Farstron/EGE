'''6740'''
def Tok(num, k): 
    alf = {0:'0', 1:'1', 2:'2', 3:'3'}
    res = ''
    while num != 0:
        res = alf[num % k] + res
        num //= k
    return res

max_R= 0 

for N in range(1,9):
    R = Tok(N,2)
    if N % 2 == 0:
        R = '10' + R
    else: 
        R = "1" + R + '01'
    max_R = int(R,2) if int(R,2) > max_R else max_R
print(max_R)

