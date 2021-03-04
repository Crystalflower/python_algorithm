# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 15
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

set_array = set(array)

frequency_of_occurrence = {i: 0 for i in set_array}

for num in array:
    frequency_of_occurrence[num] += 1

print(frequency_of_occurrence)

frequent_num = None
frequent = 0
for num, count in frequency_of_occurrence.items():
    if count > frequent:
        frequent = count
        frequent_num = num

print(frequent_num)

