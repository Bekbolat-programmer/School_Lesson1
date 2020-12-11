fin = open('f1.txt', 'r')
fout = open('f2.txt', 'w')
fin_st = fin.read().split('\n')
a, b = [], []
for i in range(len(fin_st)):
    if i % 2 == 0:
        a.append(fin_st[i])
    else:
        b.append(fin_st[i])
b.sort(reverse=True)
a.sort()
for i in a:
    fout.write("{:s}\n".format(i))
for i in b:
    fout.write("{:s}\n".format(i))