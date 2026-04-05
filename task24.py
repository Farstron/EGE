# with open('task24/24.txt') as file:
#     data = file.read()
# data = data.replace('3','e')
# data = data.replace('4','a')

# word = 'yandex'

# ml = 0
# i = 0
# l = 0
# k = 0
# while i in range(len(data)):
#     if data[i] == word[k]:
#         l += 1
#         if k < len(word) - 1:
#             k += 1
#         else:
#             k = 0
#     else:
#         ml = max(ml,l) 
#         l = 0
#         k = 0
#     i += 1
# print(ml)

# https://education.yandex.ru/ege/inf/task/c915cd87-4725-4f62-8f2f-5f5c784267df
# with open('task24/24 (1).txt') as file:
#     data = file.read()
# ml = 0
# s = ''
# for i in range(len(data)):
#     s += data[i]
#     while s.count('A') > 240:
#         s = s[1::]
#     ml = max(ml,len(s)) 
# print(ml)

#https://education.yandex.ru/ege/inf/training/24/task/1?examTaskId=083910a9-6d5d-45d9-bfe6-1ae5a008abf2&examTaskNumber=24&taskId=97e2f438-d6ce-4c55-95f5-8384f58faea4&categoryId=34289ff9-4b4d-4d32-8378-b44d98d85090
with open('task24/24 (2).txt') as file:
    data = file.read()

nums = '1234567890'
s = ''
res = []
for i in range(len(data)):
    if data[i] in nums:
        s += data[i]
    else:
        if s != '':
            res.append(int(s))
            s = ''
print(max(res))