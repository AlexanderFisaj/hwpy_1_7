# Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.

def repeat(num_repeats):
    def wrapper_func(func):
        def decorator():
            for _ in range(num_repeats):
                result = func()
            return result
        return decorator
    return wrapper_func

n = int(input('Введите количество повторений: '))

@repeat(n)
def test_func():
    print("Тестовый вывод текста на экран")

test_func()
