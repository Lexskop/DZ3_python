# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.9814] - 0.9114 или 9114

def get_numbers_list(input_list: str ) -> list:
    """
    Функция ввода чисел через пробел
    """
    numbers = []
    numbs = input(input_list).split(' ')
    for i in numbs:
        numbers.append(float(i))
    return numbers

def get_part_after_point(numbers: list) -> list:
    """
    Метод представления дробной части любого числа
    """
    for n in numbers:
        parts_list.append(float(n)-int(n))
    return parts_list

numbers = get_numbers_list('Введите несколько вещественных чисел через пробел: ')[:]
parts_list = []

get_part_after_point(numbers)
print(f'Исходный массив -> {numbers}')
print('Разница между максимальным и минимальным значением элементов ->', round(max(parts_list)-min(parts_list),10))
print('Разница в целых числах ->', ((str(round(max(parts_list)-min(parts_list),10))).split('.')[1]))