# Задача 1. Создайте пользовательский аналог метода map().

from random import randint

# Пользовательский аналог метода map()
def custom_function_map (function, iterable_object):
    return [function(element) for element in iterable_object]

# Проверка работы функции
n = 10
my_list = list(randint(10, 100) for i in range(n))
print(my_list)
negativ_numbers = custom_function_map(lambda x: -x, my_list)
print(negativ_numbers)