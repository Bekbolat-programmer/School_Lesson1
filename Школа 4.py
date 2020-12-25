def abc(a, b, c):
    a = [a, b, c]
    a.sort()
    if a[0] ** 2 == a[2] ** 2 - a[1] ** 2:
        if a[1] ** 2 == a[2] ** 2 - a[0] ** 2:
            if a[2] ** 2 == a[0] ** 2 + a[1] ** 2:
                b = 1
            else:
                b = 0
        else:
            b = 0
    else:
        b = 0
    if b == 1:
        return 'Треугольник является прямоугольным'
    else:
        return 'Треугольник не прямоугольный'


a, b, c = int(input('Введите стороны прямоугольника(через enter): ')), int(input()), int(input())
print(abc(a, b, c))