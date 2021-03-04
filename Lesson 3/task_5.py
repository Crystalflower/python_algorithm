# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

SIZE = 100
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_ = MIN_ITEM
for i in array:
    if i < 0:
        if i > max_:
            max_ = i
            if max_ == -1:
                break

print(f'Максимальный отрицательный элемент: {max_}, находится на позиции {array.index(max_)}!')
