def shift_letter(letter, shift):
    letter_new = ord(letter) - ord('a')
    shifted_letter = (letter_new + shift) % 26
    return chr(ord('a') + shifted_letter)


def lable_transformation(lable, shift):
    result = ''
    for letter in lable:
        if 'a' <= letter.lower() <= 'z':
            if letter.islower():
                result += shift_letter(letter, shift)
            else:
                result += shift_letter(letter.lower(), shift).upper()
        else:
            result += letter
    return result


lable = input('Введите строку для приобразования: ')
shift = int(input('Введите сдвиг: '))
lable_new = lable_transformation(lable, shift)
print(lable_new)