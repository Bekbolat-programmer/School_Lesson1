import random


fout = open('f1.txt', 'w')
a = []
for i in range(9):
    a.append(random.randint(-10, 10))
a.sort(reverse=True)
print(a)
for i in range(1, len(a) + 1):
    for j in range(1, i + 1):
        print(a[j - 1], end=' ', file=fout)
    print('', file=fout)
