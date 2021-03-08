# Определить, какое число в массиве встречается чаще всего.

import timeit
import cProfile
import random

SIZE = 15
SIZE_2 = 150
SIZE_3 = 150000
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
array_2 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_2)]
array_3 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_3)]


def one_func(arr):
    set_array = set(arr)

    frequency_of_occurrence = {i: 0 for i in set_array}

    for num in arr:
        frequency_of_occurrence[num] += 1

    frequent_num = None
    frequent = 0
    for num, count in frequency_of_occurrence.items():
        if count > frequent:
            frequent = count
            frequent_num = num

    return frequent_num


print(timeit.timeit('one_func(array)', number=100, globals=globals()))  # 0.0003479000000000121
print(timeit.timeit('one_func(array_2)', number=100, globals=globals()))  # 0.002167499999999989
print(timeit.timeit('one_func(array_3)', number=100, globals=globals()))  # 1.311318

cProfile.run('one_func(array)')
cProfile.run('one_func(array_2)')
cProfile.run('one_func(array_3)')


#       6 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task_1_1.py:18(one_func)
#      1    0.000    0.000    0.000    0.000 task_1_1.py:21(<dictcomp>)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}


def two_func(arr):
    set_array = set(arr)
    frequency_of_occurrence = {i: arr.count(i) for i in set_array}
    return max(frequency_of_occurrence, key=frequency_of_occurrence.get)


print(timeit.timeit('two_func(array)', number=100, globals=globals()))  # 0.00041800000000002946
print(timeit.timeit('two_func(array_2)', number=100, globals=globals()))  # 0.0023636000000000212
print(timeit.timeit('two_func(array_3)', number=100, globals=globals()))  # 2.6298985999999998

cProfile.run('two_func(array)')
cProfile.run('two_func(array_2)')
cProfile.run('two_func(array_3)')

#       17 function calls in 0.028 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.028    0.028 <string>:1(<module>)
#      1    0.002    0.002    0.028    0.028 task_1_1.py:57(two_func)
#      1    0.000    0.000    0.027    0.027 task_1_1.py:59(<dictcomp>)
#      1    0.000    0.000    0.028    0.028 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#     11    0.027    0.002    0.027    0.002 {method 'count' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def three_func(arr):
    count_number = 1
    number = None
    used_num = []
    for num in arr:
        if num in used_num:
            continue
        else:
            used_num.append(num)
        count_num = 0
        for i in arr:
            if i == num:
                count_num += 1
        if count_num > count_number:
            count_number = count_num
            number = num
    return number, count_number


print(timeit.timeit('three_func(array)', number=100, globals=globals()))  # 0.0006781000000000148
print(timeit.timeit('three_func(array_2)', number=100, globals=globals()))  # 0.00560390000000055
print(timeit.timeit('three_func(array_3)', number=100, globals=globals()))  # 6.041401500000001

cProfile.run('three_func(array)')
cProfile.run('three_func(array_2)')
cProfile.run('three_func(array_3)')

#       15 function calls in 0.061 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.061    0.061 <string>:1(<module>)
#      1    0.061    0.061    0.061    0.061 task_1_1.py:86(three_func)
#      1    0.000    0.000    0.061    0.061 {built-in method builtins.exec}
#     11    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


'''
Вывод: Наиболее благоприятен первый способ, так как count и append каждый раз перебирают список заново.
'''
