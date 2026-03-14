'''22269'''
def Tok(num,k):
    alf = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6'}
    res=''
    while num != 0:
        res = alf[num % k] +res
        num //= k
    return res
bR = -1
bN = None
for N in range(10000):
    R = Tok(N,5)
    s = R.replace('1','#').replace('4','1').replace('#','4')
    if R[-1]  == '0':
        r = '33' + s
    else:
         r = '3' + r[1:] + '42'
    M = int(r,5)
    if M < 1922:
        if M > bR:
            bR = M
            bN = N
            print(bN)
            break