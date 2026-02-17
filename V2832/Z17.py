'''2017'''

F=[int(s) for s in open ('V2832/files/17_2017.txt')]
M =[x for x in F  if x < 10001]
res = []
for i in range(len(F)):
    ed = [F[i]]
    for el in ed:
        if el % 16 == 11 and el  % 7 == 0 and el % 13 != 0 and el % 19 != 0: 
            res.append(sum(ed))
print(sum(res), len(res)) 
print(10**7)

