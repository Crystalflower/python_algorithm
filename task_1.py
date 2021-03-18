# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random

array = [random.randrange(-100, 100) for _ in range(10)]

print(array)

print('*' * 50)


def bubble(arr):
    count = 1
    while count < len(arr):
        transposition = 0
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                transposition += 1
        print(arr)
        if transposition == 0:
            return
        count += 1


bubble(array)

print('*' * 50)

print(array)


