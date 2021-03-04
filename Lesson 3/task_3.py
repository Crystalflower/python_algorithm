# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_ = MIN_ITEM
min_ = MAX_ITEM

for i in array:
    if i > max_:
        max_ = i
    if i < min_:
        min_ = i

max_index = array.index(max_)
min_index = array.index(min_)

array[max_index], array[min_index] = array[min_index], array[max_index]

print(array)
