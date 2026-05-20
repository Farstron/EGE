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
#      alf = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:'5',6:'6',7:'7', 8:'8', 9:'9', 10:'A'}
#      res = ''
#      while num != 0:
#          res = alf[num % k] + res
#          num //= k
#      return res

# print(ToK(2969-1, 5))

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
# c = 0 
# for el in PR("012345678", repeat=5):
#     el="".join(el)
#     if (el.count('3') == 2 and el[0] != '0' and
#         ('12' not in el and '21' not in el 
#          and '23' not in el and '32' not in el 
#          and '52' not in el and '25' not in el 
#          and '72' not in el and '27' not in el)):
#         c += 1
# print(c)

'''
Сколько слов длины 4, начинающихся с согласной буквы и заканчивающихся гласной буквой, можно составить из букв М, Е, Т, Р, О? 
Каждая буква может входить в слово несколько раз. Слова не обязательно должны быть осмысленными словами русского языка.
'''

# # Инициализация счетчика для подсчета подходящих комбинаций
# c = 0

# # Перебираем все возможные комбинации из букв слова "МЕТРО"
# # PR - функция, генерирующая перестановки с повторениями
# # repeat=4 означает, что генерируются комбинации длиной 4 символа
# for el in PR("МЕТРО", repeat=4):
    
#     # Преобразуем кортеж символов в строку
#     # Например, ('М', 'Е', 'Т', 'Р') превращается в "МЕТР"
#     el = "".join(el)
    
#     # Проверяем условия для текущей комбинации:
#     # 1. Первый символ должен быть одной из букв "МРТ"
#     # 2. Последний символ должен быть одной из букв "ЕО"
#     if (el[0] in "МРТ") and (el[-1] in 'ЕО'):
        
#         # Если условия выполнены, увеличиваем счетчик
#         c += 1

# # Выводим итоговое количество подходящих комбинаций
# print(c)




'''
Все 4-⁠буквенные слова, составленные из букв М, А, Р, Т, записаны в алфавитном порядке.

Вот начало списка:

1.АААА
2.АААМ
3.АААР
4.АААТ
5.ААМА

Запишите слово, которое стоит на 250-⁠м месте от начала списка.
'''

# def Tok(num, k):
#     alf= {0: "0", 1:"1", 2: "2", 3: "3"}
#     res = ""
#     while num != 0: 
#         res = alf[num % k] + res 
#         num = num // k
#     return res
# print("ОТВЕТ: ", Tok(250-1, 4))


'''
Все пятибуквенные слова, составленные из букв ИЮНЬ записаны в алфавитном порядке и пронумерованы. Вот начало этого списка:

ИИИИИ
ИИИИН
ИИИИЬ
ИИИИЮ
ИИИНИ
ИИИНН

Под каким номером в списке идёт последнее слово, в котором содержится ровно 2 гласные буквы?
'''

from itertools import product as PR

# c = 0
# last_number = 0
# for el in PR('ИНЬЮ', repeat=5):
#     c += 1
#     el = ''.join(el)
#     if el.count('И') + el.count('Ю') == 2:
#         last_number = c
# print(last_number)

# print(int("31020", 4)+1)

'''Определите количество 13-ричных семизначных чисел, 
в записи которых не менее двух цифр 5 и никакие две чётные и две нечётные цифры не стоят рядом.'''

# н ч н ч н ч н (0,1,2,3,4,5,6,7,8,9,10,11,12) -> 6 * 7 * 6 * 7 * 6 * 7 * 6 = 444528 * 2
# ч н ч н ч н ч (0,1,2,3,4,5,6,7,8,9,10,11,12) -> 6 * 6 * 7 * 6 * 7 * 6 * 7 = 444528
# C = 0
# for el in PR('13579B','02468AC','13579B','02468AC','13579B','02468AC','13579B'):
#     el = ''.join(el)
#     if el.count('5') >= 2:
#         C += 1
# for el in PR('02468AC','13579B','02468AC','13579B','02468AC','13579B','02468AC'):
#     el = ''.join(el)
#     if el.count('5') >= 2:
#         C += 1
# print(C)


# https://education.yandex.ru/ege/inf/task/86d21473-bf55-4b4d-99d9-d620244843ad
# from itertools import product as PR
# c= 0
# for el in PR('АБВОСТУ', repeat=5):
#     c+=1
#     el = ''.join(el)
#     if 'А' in el or 'О' in el:
#         continue
#     if len(set(el)) != 5:
#         continue
#     if el[-2:] == 'СБ':
#         print(c,el)
#         break


# https://education.yandex.ru/ege/inf/task/4c623ce7-3e25-4a25-9660-2d139d520811
# from itertools import product as PR
# c = 0
# ln = 0
# for el in PR('АЙЛМ', repeat= 5):
#     c+=1
#     el = ''.join(el)
#     if el.count('М') >=2:
#         continue
#     if "ЛЛ" not in el:
#         ln = c
# print(ln)

# https://education.yandex.ru/ege/inf/task/08a16fb2-3773-4f00-8961-cfa21b2e65a9

# from itertools import product as PR
# c = 0
# for el in PR('ГИПЕРБОЛА', repeat=6):
#     el = ''.join(el)
#     if el[0] not in "ИЕОА" and el[-1] not in 'ИЕОА':
#         f = True
#         for el1 in PR('ГПРБЛ', "ИЕОА", "ГПРБЛ"):
#             el1 = ''.join(el1)
#             if el1 in el:
#                 f = False
#         if f:
#             c+=1
# print(c)
    


# https://education.yandex.ru/ege/inf/task/701d192b-06f1-4cbe-8bc7-6e2d63be9e03

# from itertools import product as PR
# c=0
# ln=0
# for el in PR('АЕЛПРЬ', repeat=5):
#     c+=1
#     el=''.join(el)
#     if el[0] not in 'ЬР' and el.count('Л') >= 2:
#         if c % 2==0: 
#             ln = c
# print(ln)

    
# https://education.yandex.ru/ege/inf/task/6fbcf8cd-d727-4ea5-86b2-12193523ab8b
# from itertools import product as PR
# c= 0
# for el in PR("ВОЗДУХ",repeat=5):
#     el= ''.join(el)
#     if not(el.count('О') + el.count('У')) == 1:
#         continue
#     if 'О' in el:
#         pos = el.find('О')
#     else: 
#         pos = el.find('У')
#     if (pos > 0 and el[pos-1] in 'ВХ') or (pos < 4 and el[pos+1] in 'ВХ'):
#         continue
#     c+=1
# print(c)


# https://education.yandex.ru/ege/inf/task/701d192b-06f1-4cbe-8bc7-6e2d63be9e03

# from itertools import product as PR 
# c= 0
# ln = 0 
# for el in PR('АЕЛПРЬ',repeat=5):
#     c+=1
#     el=''.join(el)
#     if el[0] not in 'РЬ' and el.count('Л') >= 2: 
#         if c % 2 == 0: 
#             ln = c
# print(ln)


# https://education.yandex.ru/ege/inf/task/4e2f69a3-5052-46b2-bea8-9de0b660c3d1

# from itertools import product as PR
# c=0
# for el in PR('0123456789ABCDEF',repeat=8):
#     el=''.join(el)
#     if el.count('0') == 2 and int(el,16) % 2 == 0:
#             c+=1
# print(c) 
            


# https://education.yandex.ru/ege/inf/task/e4bb815e-4a86-4423-ab51-7b896e96d693

# from itertools import product as PR
# c=0
# for el in PR('ГИРЛЯНДА', repeat=9):
#     el = ''.join(el)
#     if el.count('A') == 1:
#         f = True
#         for el1 in PR('ГРЛНД','А', 'ГРЛНД'):
#             el1 =''.join(el1)
#             if el1 in el:
#                 f= False
#         if f:
#             c +=1
# print(c)

# from itertools import product as PR
# c=0
# ch = '01234567'
# chet= '0246'
# nechet = '1357'
# for el in PR(chet, nechet, chet,nechet,chet,nechet,chet):
#     el=''.join(el)
#     if el[0] == 0:
#         continue
#     if len(set(el)) != 5:
#         continue
#     c+= 1
# print(c)


# from itertools import product as PR
# c=0
# for el in PR('АЕКЛ',repeat=5):
#     c+=1
#     el =''.join(el)
#     if el.count('А') <=1 and el.count('К') == 2 and el.count('Л') == 0: 
#         print(c,el)
#         break

# from itertools import product as PR
# c=0
# for el in PR('АЕЛПРЬ', repeat=6):
#     c+=1
#     el=''.join(el)
#     if el[0] not in 'АЛ' and el.count('П') >= 2 and c % 2== 1:
#         print(c,el)
#         break

from itertools import product as PR
c=0 
for el in PR('0123456789ABCD',repeat = 5):
    el = ''.join(el)
    f = True 
    for i in range(4):
        a,b = el[i], el[i+1]
        if (a in 'ABCD' and b in '13579') or (a in '13579' and b in 'ABCD'):
            f = False
            break
    if f:
        c+=1
print(c)