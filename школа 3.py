fin = open('f1.txt', 'r')
fin_st = fin.read().split('\n')
sma, smb = 1, 0
a, b = [], []
for i in fin_st:
    if int(i) % 5 == 0:
        a.append(int(i))
    else:
        b.append(int(i))
for i in a:
    sma *= int(i)
print(11 % 5)
print(sma, sum(b), a, b)
fin.close()
fin = open('f1.txt', 'w')
fin.write("{:s}\n".format(str(sma)))
fin.write("{:s}\n".format(str(sum(b))))
fin.close()