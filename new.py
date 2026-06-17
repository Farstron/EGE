# from  itertools import product as PR
# c= 0
# for el in PR('АВЛОР',repeat=4):
#     c +=1
#     el = ''.join(el)
#     if el[0] == 'Л':
#         print(c)
#         break

# k = 0
# for s in open ('task9/9(8).txt'):
#     n = sorted([int(i) for i in s.split()])
#     n1 = [i for i in n if n.count(i) == 1]
#     if n[3] < n[0] + n[1] + n[2]:
#         if len(n1) == 4:
#             k +=1
# print(k)

k = 0   
from ipaddress import * 
n = ip_network('172.16.168.0/255.255.248.0', 0)
for i in n:
    if (bin(int(i))[2:]).count('1') % 5 != 0:
        k +=1
print(k)
