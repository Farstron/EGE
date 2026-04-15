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
# with open('task24/24 (2).txt') as file:
#     data = file.read()

# nums = '1234567890'
# s = ''
# res = []
# for i in range(len(data)):
#     if data[i] in nums:
#         s += data[i]
#     else:
#         if s != '':
#             res.append(int(s))
#             s = ''
# print(max(res))


# https://education.yandex.ru/ege/inf/task/b80b725b-df8b-407d-b120-941e53aa5df9

# with open('task24/24(3).txt') as file:
#     data = file.read()
# left = 0
# res = []
# state = False
# right = 0
# while right < len(data):
#     if data[left:right].count('A') > 100 or  data[left:right].count('O') > 100:
#         if not state:
#             res.append(len(data[left:right-1]))
#             state = True
#         else:
#             left += 1
#     else:
#         right += 1
#         state = False
# print(max(res))

# s = 'RRGOAGDNDNRNORDGNNGNARON'
# s = 'RNOAGD'
# print(len(s) == len(set(s)))


# https://education.yandex.ru/ege/inf/task/dc2aa40a-ee08-4e9c-b43f-81fbccbd1d7e

# with open('task24/24(5).txt') as file:
#     data = file.read()
# res = []
# left = 0
# state = False
# right = 0
# while right < len(data):
#     if len(data[left:right]) != len(set(data[left:right])):
#         if not state:
#             res.append(len(data[left:right-1]))
#             state = True
#         else:
#             left += 1
#     else:
#         right +=1
#         state = False
# print(max(res))


# https://education.yandex.ru/ege/inf/task/37e7362a-fc21-4cc7-acb1-3859dde6d2ef
'''!!!!!!!!!!!!!!!!!!!!!!_________________'''

with open('task24/24(6).txt') as file:
    data = file.read()
res = []
left = 0
state = False
right = 0
nums = '123'
buks = 'KLMN'
while right < len(data):
    if data[left:right].count(buks)*2 == data[left:right].count(nums):
        if not state:
            res.append(len(data[left:right]))
            state = True
        else:
            left += 1
    else: 
        right +=1
        state = False
print(max(res))