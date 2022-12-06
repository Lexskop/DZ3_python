# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def convert_to_X_numeral_system(num: int) -> list:
    """
    Метод вычисления числа из десятичной системы системы в любую
    """
    if not num:
        sis.reverse()
        return sis
    sis.append(num % numeral)
    convert_to_X_numeral_system(num // numeral)

print('Приветствую! Эта программа преобразует любое число на любую систему счислений.')
num = int(input('Введите число: '))
sis = []
numeral = int(input('Введите в какую систему счислений перевести(просто число) -> '))
convert_to_X_numeral_system(num)
print(f'Число {num} в {numeral} системе -> ', end='')
for i in sis:
    print(i, end='')