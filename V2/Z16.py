'''8953'''
def F(n, mem):
    if n in list(mem.keys()):
        return mem[n]
    if n >= 10000:
        return 1
    if n < 10000 and n % 2 == 0:
        return F(n+3,mem) + 7
    return F(n+1,mem) - 3

mem = {}
for n in range(10100,49,-1):
    mem[n] = F(n, mem)

print(F(50, mem) - F(57, mem))

def Ffac(n, mem):
    if n in list(mem.keys()):
        return mem[n]
    if n > 1:
        return Ffac(n-1,mem)*n
    return 1

mem2 = {}
for n in range(2027):
    mem2[n] = Ffac(n, mem2)

print((Ffac(2026, mem2) - Ffac(2025, mem2))/Ffac(2025, mem2))