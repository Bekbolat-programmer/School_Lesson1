t = input('Введите текст: ')
r = len(t) ** 0.5
if float(round(r)) == r:
    n = round(r)
else:
    n = int(r) + 1
end = [[" "] * n for i in range(n)]
rt = []
a = n
for i in range(n):
    end[i][0] = t[i]
for i in range(n - 1, 0, -1):
    for j in range(2):
        rt.append(t[a:a + i])
        a += i
ot = 2
sh = [1, 0, 0, 0]
for i in range(0, len(rt)):
    if ot == 1:
        for j in range(len(rt[i])):
            end[sh[ot - 1] + j][sh[ot - 1]] = rt[i][j]
        sh[ot - 1] = sh[ot - 1] + 1
        ot += 1
    elif ot == 2:
        for j in range(len(rt[i])):
            end[n - sh[ot - 2]][1 + j + sh[ot - 1]] = rt[i][j]
        sh[ot - 1] = sh[ot - 1] + 1
        ot += 1
    elif ot == 3:
        for j in range(len(rt[i])):
            end[n - 1 - sh[ot - 2] - j][n - 1 - sh[ot - 1]] = rt[i][j]
        sh[ot - 1] = sh[ot - 1] + 1
        ot += 1
    elif ot == 4:
        for j in range(len(rt[i])):
            end[sh[ot - 1]][n - 1 - sh[ot - 2] - j] = rt[i][j]
        sh[ot - 1] = sh[ot - 1] + 1
        ot = 1
for i in range(n - 1):
    print(''.join(end[i]), end="")
print(''.join(end[n - 1]))