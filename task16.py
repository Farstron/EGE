# № 24537 (Уровень: Базовый)
def F(n,mem):
    if n in list(mem.keys()):
        return mem[n]
    if n < 10:
        return n + 10
    if n >= 10:
        return F(n-8,mem) + 2**n
mem = {}
for n in range(1, 4001):
    mem[n] = F(n,mem)

print((F(4000,mem ) + 2 * F(3992,mem))/F(3984,mem))        