"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers_list):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers_list]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(*numbers, filter):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter == ODD:
        return [number for number in numbers if number % 2 == 0]
    if filter == EVEN:
        return [number for number in numbers if number % 2]
