# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше.

import random

n = 5

array = [random.randrange(0, 10) for _ in range(2 * n + 1)]

print(array)


def mediate(arr):
    len_ = len(arr)
    mediate_len = (len_ - 1) / 2
    for i in range(len_):
        more = []
        less = []
        equal = []
        for j in range(len_):
            if i == j:
                continue
            if arr[j] > arr[i]:
                more.append(arr[j])
            elif arr[j] < arr[i]:
                less.append(arr[j])
            elif arr[j] == arr[i]:
                equal.append(arr[j])
            if len(more) > mediate_len or len(less) > mediate_len:
                break
        if len(more) > mediate_len or len(less) > mediate_len:
            continue
        if len(more + less + equal) == len_ - 1:
            return arr[i]


print(mediate(array))


print(sorted(array))
print(sorted(array)[n])
