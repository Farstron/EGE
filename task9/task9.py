with open('task9/task9.txt') as file:
    data = [list(map(int,el.split('\t'))) for el in file.read().split('\n')]
cols = [[data[i][0] for i in range(4)], [data[i][1] for i in range(4)],[data[i][2] for i in range(4)]]
print(cols)
for i in range(len(data)):
    if max(data[i]) % 10 == 0 and data[i].count(max(data[i])) == 3 and len(set(data[i])) == 5:
        print(i+1)
        break