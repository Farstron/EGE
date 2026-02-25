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

def F(n, mem):
    if n in list(mem.keys()):
        return mem[n]
    if n <= 10:
        return n    
    else: 
        return (n - 7 + F(n-21,mem))

mem = {}
for n in range(10, 185735,1):
    mem[n] = F(n,mem)
    print(f'{n}: {mem[n]}')

print((F(185734,mem) - F(185659,mem))/F(40,mem))