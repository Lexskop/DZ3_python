# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def get_fibonacci(num):
    """
    Метод вычисления Фибоначчи
    """
    if num == 0:
        fibonacci = [0]
        return fibonacci
    fibonacci = [0,1]
    for i in range(num-1):
        fib1 = fibonacci[i]
        fib2 = fibonacci[i+1]
        fib = fib1+fib2
        fibonacci.append(fib)
    return fibonacci

def get_negafibonacci(fibonacci):
    """
    Метод вычисления Негафибоначчи
    """
    negafibonacci = []
    n = 0
    for i in fibonacci:
        negafib = ((-1)**(n+1))*i
        negafibonacci.append(negafib)
        n+=1
    negafibonacci.reverse()
    return negafibonacci

fibonacci = get_fibonacci(int(input('Введите число -> ')))
negafibonacci = get_negafibonacci(fibonacci)

print(negafibonacci[:-1]+fibonacci)