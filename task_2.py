def fibonacci(n: int) -> int:
    """
    Функция, вычисляющая n-ое число Фибоначчи.
    """
    if n <= 0 or not isinstance(n, int):
        return "n должно быть натуральным числом"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[-1]


# Тестовые данные
print(fibonacci(3))
print(fibonacci(0))
print(fibonacci(-8))
print(fibonacci(8.5))
