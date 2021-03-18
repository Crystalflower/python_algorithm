# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

array = [random.uniform(0, 50) for _ in range(10)]

print(array)


def merge(arr):
    count = len(arr)
    if count <= 1:
        return arr

    a = merge(arr[:count // 2])
    b = merge(arr[count // 2:])
    m_list = a + b

    a_i = b_i = 0
    sort_arr = []

    for _ in range(len(m_list)):
        if a_i < len(a) and b_i < len(b):
            if a[a_i] <= b[b_i]:
                sort_arr.append(a[a_i])
                a_i += 1
            else:
                sort_arr.append(b[b_i])
                b_i += 1
        elif a_i == len(a):
            sort_arr.append(b[b_i])
            b_i += 1
        elif b_i == len(b):
            sort_arr.append(a[a_i])
            a_i += 1
    return sort_arr


print(merge(array))
