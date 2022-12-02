# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

def calc():
    """
    Метод расчета произведения пар чисел списка
    """
    input_list = []
    for i in input('Введите числа через пробел -> ').split():
        input_list.append(int(i))
    print('Получили список -> ',input_list)
    if len(input_list) % 2 == 0: 
        result = [0 for i in range(int(len(input_list)/2))]
    if len(input_list) % 2 == 1: 
        result = [0 for i in range(int(len(input_list)/2 + 1))]
    # print(result) # отладка нужного количества значений в result
    for i in range(int(len(result))):
        if i < int(len(input_list)) / 2 or int(len(result)) % 2 == 0:
            result[i] = input_list[i] * input_list[len(input_list)-1-i]
        elif i == int(len(result) / 2) or int(len(input_list)) % 2 == 1:
            result[i] = input_list[i]*input_list[i]
    print('Рассчитали список произведения пар чисел -> ',result)
    user_another_try()

def user_another_try():
    """
    Метод для возможности не закрывая программу воспользоваться ею еще раз
    """
    user_choice = input('Вы хотите продолжить работу с программой? Да - Y, Нет - N - > ')
    while user_choice.lower() != 'y' and user_choice.lower() != 'n' and user_choice.lower() != 'x':
        user_choice = input('Пожалуйста, введите верное решение. Если хотите продолжить работу - введите Y, если желаете закрыть программу - введите N или X -> ')
    if user_choice.lower() == 'y':
        calc()
    else:
        print('Bye!')


print('Приветствую! Эта программа найдёт сумму элементов списка, стоящих на нечётной позиции.')
calc()