"""
Простые числа в заданном диапазоне.
Необходимо разработать функцию prime_numbers(low, high), где low и high – нижняя и верхняя
границы диапазона, в котором надо найти эти числа. Функция должна возвращать список с
числами, отсортированными по возрастанию.
"""


def prime_numbers(low, high):
    numbers = []

    try:
        if int(low) == low and int(high) == high:
            low = int(low)
            high = int(high)

        for i in range(low, high + 1):
            for j in range(2, i + 1):
                if i % j == 0 and i != 2:
                    break
                elif i // j <= j:
                    numbers.append(i)
                    break

    except TypeError:
        return numbers

    return numbers

