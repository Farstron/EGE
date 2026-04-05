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


with open('task24/24 (1).txt') as file:
    data = file.read()

word = 'ADENXY!'

ml = 0
i = 0
l = 0
k = 0
s = ''
while i in range(len(data)):
    if data[i] == word[k]:
        s += data[i]
    elif data[i] == word[k+1]:
        s += data[i]
        if k < len(word) - 2:
            k += 1
        else:
            k = 0
    else:

        ml = max(ml,len(s)) 
        l = 0
        k = 0
    i += 1
print(ml)
