'''
Все пятибуквенные слова, в составе которых могут быть только буквы П, А, Р, У, С, записаны в 
алфавитном порядке и пронумерованы начиная с 1.
Ниже приведено начало списка.
1.  ААААА => 0
2.  ААААП => 1
3.  ААААР => 2
4.  ААААС
5.  ААААУ
6.  АААПА

A = 0
П = 1
Р = 2
С = 3
У = 4

УСССС
43333_5 -> (x_10)+1


Под каким номером в списке идёт последнее слово, которое содержит не более одной буквы У и не содержит букв А, стоящих рядом?

№5 7 8 11 13
'''

# print(int("43333",5)+1)

# def ToK(num, k):
#     alf = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:'5',6:'6',7:'7', 8:'8', 9:'9', 10:'A'}
#     res = ''
#     while num != 0:
#         res = alf[num % k] + res
#         num //= k
#     return res

# print(ToK(2969-1, 5)

# №4588
# print(int("3233", 4)+1)

# №7201
# def Tok(num,k):
#     alf = {0:"0", 1:"1", 2:"2", 3:'3', 4:'4'}
#     res = " "
#     while num != 0:
#         res = alf[num % k] + res
#         num = num // k 
#     return res
# print(Tok(250-1,4))

# № 57415
# print (int("3210", 4)+1)

# №8658
# def Tok(num,k):
#     alf = {0:"0", 1:'1',2:'2',3:'3'}
#     res = ""
#     while num != 0:
#         res = alf[num % k] + res
#         num = num // k
#     return res 
# print(Tok(201 - 1, 3))

'''
Митрофан составляет коды из букв, входящих в слово МИТРОФАН. Код должен состоять из 6 букв, буквы в коде не должны повторяться, 
согласных в коде должно быть больше, чем гласных, две гласные буквы нельзя ставить рядом. Сколько кодов может составить Митрофан?
'''
from itertools import product as PR
from itertools import permutations as PE

# for el in PR('123',repeat=2):
#     print(el)

# print("__________")

# for el in PE('123', r=2):
#     print(el)

# for el in PR('123','456'):
#     print(el)

# c = 0
# for el in PE('МИТРОФАН', r = 6):
#     el = ''.join(el)
#     if (((el.count('М') + el.count('Т') + el.count('Р') + el.count('Ф') + el.count('Н')) > (el.count('И') + el.count('О') + el.count('А'))) 
#         and (('ИИ' not in el) and ('ИА' not in el) and ('ИО' not in el) and ('АИ' not in el) and ('АО' not in el) and ('АА' not in el) and ('ОИ' not in el) and ('ОА' not in el) and ('ОО' not in el))):
#         c += 1
# print(c)

# c = 0
# gl = [''.join(el) for el in PR('ИАО',repeat=2)]
# for el in PE('МИТРОФАН', r = 6):
#     el = ''.join(el)
#     if (((el.count('И') + el.count('О') + el.count('А')) < 3) and (max([el.count(x) for x in gl]) == 0)):
#         c += 1
# print(c)


'''
Игорь составляет пятизначные числа, используя цифры девятеричной системы счисления. 
Сколько различных чисел может составить Игорь, в которых ровно две цифры 3 и нечётные цифры не стоят рядом с цифрой 2?
'''
c = 0 
for el in PR("012345678", repeat=5):
    el="".join(el)
    if (el.count('3') == 2 and el[0] != '0' and
        ('12' not in el and '21' not in el 
         and '23' not in el and '32' not in el 
         and '52' not in el and '25' not in el 
         and '72' not in el and '27' not in el)):
        c += 1
print(c)