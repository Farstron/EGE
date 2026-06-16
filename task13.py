# print(bin(176)[2:])
# print(bin(160)[2:])
# print(int("11100000",2))
# print(bin(101)[2:])
# print(bin(64)[2:])
# print(int('11000000',2))
# print(bin(124)[2:])
# print(bin(252)[2:])
# print(int("01111111",2))
# print(int('11111110',2))
# print(bin(101)[2:])
# print(bin(64)[2:])
# print(int('11000000',2))
# print("0"*(8-len(bin(23)[2:]))+bin(23)[2:])
# print(bin(192)[2:])
# print(int('10111111',2))
# print(int('11111110',2))
# print(bin(128)[2:])
# print(bin(192)[2:])
# print(int("10000000", 2))
# print(bin(137)[2:])
# print(bin(240)[2:])
# print(int("10000000", 2))
# print(bin(128)[2:])
# print(bin(240)[2:])
# print(bin(73)[2:])
# print(bin(75)[2:])
# print(int('11111101', 2))
# print(bin(42)[2:])
# print(bin(136)[2:])
# print(int('1011101',2))

'''В терминологии сетей TCP/IP маской сети называют двоичное число, которое показывает, какая часть IP-адреса узла сети относится к адресу сети, а какая — к адресу узла в этой сети.
Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу узла и маске сети.
У двух узлов из одной сети IP-адреса 61.58.73.42 и 61.58.75.136. 
Определите маску сети с наибольшим количеством единиц, для которой это возможно.
Для найденного значения маски посчитайте количество узлов (устройств), в двоичной записи IP-адреса которых нечётное количество единиц.
Примечание: IP-адреса подсети и широковещательной передачи (broadcast) не могут быть использованы для устройств.'''


# print('.'.join(['0'*(8-len(bin(int(el))[2:]))+ bin(int(el))[2:] for el in '61.58.73.42'.split('.')]))
# print('.'.join(['0'*(8-len(bin(int(el))[2:]))+ bin(int(el))[2:] for el in '61.58.75.136'.split('.')]))

# from itertools import product as pr
# c = 0
# for el in pr('01', repeat=10):
#     if ''.join(el) != '0000000000' and ''.join(el) != '1111111111':
#         el = '0011110100111010010010' + ''.join(el)
#         if el.count('1') % 2 == 1:
#             c += 1
# print(c)

# print(bin(224)[2:])  '11100000'
# print(bin(96)[2:])   '01100000'
#                      '01100000'


# print(bin(252)[2:])
# print(bin(83)[2:])
# print(int('01010000',2))
# print(bin(62)[2:])
# print(bin(68)[2:])
# print(bin(248)[2:])
# print(int('01000000',2))
# print(int('01000111',2))
# print(bin(128)[2:])
# print(bin(192)[2:])
# print(bin(168)[2:])
# print(bin(32)[2:])
# print(bin(160)[2:])
# print(bin(240)[2:])


# from ipaddress import *
# net=ip_network('205.99.68.249/255.255.248.0',0)
# print(net[-2])

# from ipaddress import *
# net = ip_network('68.203.243.87/255.255.224.0',0)
# print(net[-2])

# from ipaddress import *
# net  = ip_network('172.17.167.18/255.255.240.0',0)
# print(net[-2]) 

# from ipaddress import *
# net = ip_network('152.191.15.163/255.244.0.0',0)
# print(net[1])

# k = 0
# from  ipaddress import *
# num = ip_network('122.159.136.144/255.255.255.248',0)
# for ip in num:
#     if bin(int(ip)).count('1') % 4 != 0:
#         k +=1
# print(k)

# k = 0 
# from ipaddress import *
# n = ip_network('192.168.32.160/255.255.255.240',0)
# for i in n:
#     if (bin(int(i))[2:]).count('1') % 2 ==0:
#         k+=1
# print(k)

from ipaddress import *
n = ip_network('153.107.147.227/255.255.224.0',0)
print(n[-2])