# № 24537 (Уровень: Базовый)
# def F(n,mem):
#     if n in list(mem.keys()):
#         return mem[n]
#     if n < 10:
#         return n + 10
#     if n >= 10:
#         return F(n-8,mem) + 2**n
# mem = {}
# for n in range(1, 4001):
#     mem[n] = F(n,mem)

# print((F(4000,mem ) + 2 * F(3992,mem))/F(3984,mem))    

# 24891

# def F(n, mem):
#     if n in list(mem.keys()):
#         return mem[n]
#     if n <= 10:
#         return n    
#     else: 
#         return (n - 7 + F(n-21,mem))

# mem = {}
# for n in range(10, 185735,1):
#     mem[n] = F(n,mem)
#     print(f'{n}: {mem[n]}')

# print((F(185734,mem) - F(185659,mem))/F(40,mem))


'''23200'''

# def F(n,mem): 
#     if n in list(mem.keys()):
#         return mem[n]
#     if n < 10:
#         return n
#     if n >= 10:
#         return 3*n + F(n - 3, mem)
# mem = {}
# for n in range(1, 6251):
#     mem[n] = F(n,mem)
# print((F(6250,mem) + 2 * F(6244,mem)) // F(6238,mem))


'''19708'''
# def F(n,mem):
#     if n in list(mem.keys()):
#         return mem[n]
#     if n < 13:
#         return 13
#     if n>= 13 and n % 5 != 0:
#         return 13 - F(n-1,mem)
#     if n >= 13 and n % 5 == 0:
#         return 13 + F(n-1,mem)
# mem = {}
# for n in range(1,3014):
#     mem[n] = F(n,mem)
# print(F(3013,mem))


# #26493
# def G(n,memG):
#     if n in list(memG.keys()):
#         return memG[n]
#     if n >= 52000:
#         return n/10 + 30
#     return G(n+1,memG) - 1/2

# def F(n,memF, memG):
#     if n in list(memF.keys()):
#         return memF[n]
#     if n >= 67:
#         return n
#     return 3*(G(n-2, memG)-1)

# memG = {}
# for n in range(53000,0,-1):
#     memG[n] = G(n,memG)

# memF = {}
# for n in range(10007,0,-1):
#     memF[n] = F(n,memF, memG)

# print(F(10007,memF,memG))

'''25400'''
def G(n,meG):
    if n in list(meG.keys()):
        return meG[n]
    if n >= 28:
        return G(n-5,meG) - 15
    if n < 28:
        return 3 * n - 4
    
def F(n,meF,meG):
    if n in list(meF.keys()):
        return meF[n]
    if n < 31054:
        return F(n + 4,meF,meG) + 3020
    if n >= 31054:
        return 3 * (G(n-2,meG)-15)
    
meG = {}
for n in range(1,31200):
    meG[n] = G(n,meG)

meF = {}
for n in range(31200,1,-1):
    meF[n] = F(n,meF,meG)

print(F(15,meF,meG))