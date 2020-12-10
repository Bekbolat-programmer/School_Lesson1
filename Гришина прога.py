def lt_b(a, b):
    a = ord(a) - ord('a')
    a = (a + b) % 26
    return chr(ord('a') + a)


def a_tr(a, b):
    result = ''
    for lt in a:
        if 'a' <= lt.lower() <= 'z':
            if lt.islower():
                result += lt_b(lt, b)
            else:
                result += lt_b(lt.lower(), b).upper()
        else:
            result += lt
    return result


print('Введите строку для приобразования: ')
a = input()
print('Введите сдвиг: ')
b = int(input())
a = a_tr(a, b)
print(a)