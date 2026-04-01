# with open('task9/task9.txt') as file:
#     data = [list(map(int,el.split('\t'))) for el in file.read().split('\n')]
# cols = [[data[i][0] for i in range(4)], [data[i][1] for i in range(4)],[data[i][2] for i in range(4)]]
# print(cols)
# for i in range(len(data)):
#     if max(data[i]) % 10 == 0 and data[i].count(max(data[i])) == 3 and len(set(data[i])) == 5:
#         print(i+1)
#         break

# c=0
# with open('task9/task9(1).txt') as file:
#     data = [list(map(int,el.split('\t'))) for el in file.read().split('\n')]
# for i in range(len(data)):
#     if len(set(data[i])) == 4 and max(data[i]) < (sum(data[i]) - max(data[i])):
#         c+=1
# print(c)
        
with open('task9/task9(2).txt') as file:
    data = [list(map(int,el.split('\t'))) for el in file.read().split('\n')]
c = 0
for i in range(len(data)):
    for el in set(data[i]):
        if data[i].count(el) == 3 and len(set(data[i])) == 5:
            if el ** 2 > (sum(data[i]) - 3 * el):
                c += 1
print(c)

