# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

import timeit
import cProfile

DEFAULT_START_NUM = -2
DEFAULT_START_SUMMA = 0

N = 100
N_FOR_FIRST = 500
N_2 = 900
N_3 = 10_000


def one_func(count, start_num, sum_):
    result = start_num / -2
    count -= 1
    sum_ += result
    if count == 0:
        return f'{result}\nСумма последовательности: {sum_}'
    return f'{result}, {one_func(count, result, sum_)}'


print(timeit.timeit('one_func(N, DEFAULT_START_NUM, DEFAULT_START_SUMMA)', number=100, globals=globals()))
# 0.020949000000000002
print(timeit.timeit('one_func(N_FOR_FIRST, DEFAULT_START_NUM, DEFAULT_START_SUMMA)', number=100, globals=globals()))
# 0.15095399999999998
print(timeit.timeit('one_func(N_2, DEFAULT_START_NUM, DEFAULT_START_SUMMA)', number=100, globals=globals()))
# 1.086934

cProfile.run('one_func(N, DEFAULT_START_NUM, DEFAULT_START_SUMMA)')
cProfile.run('one_func(N_FOR_FIRST, DEFAULT_START_NUM, DEFAULT_START_SUMMA)')
cProfile.run('one_func(N_2, DEFAULT_START_NUM, DEFAULT_START_SUMMA)')

#       903 function calls (4 primitive calls) in 0.016 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.016    0.016 <string>:1(<module>)
#  900/1    0.016    0.000    0.016    0.016 task_1_2.py:16(one_func)
#      1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def two_func(n):
    array = [1]
    for _ in range(n - 1):
        array.append(array[-1] / -2)
    return sum(array)


print(timeit.timeit('two_func(N)', number=100, globals=globals()))  # 0.0011338000000000736
print(timeit.timeit('two_func(N_2)', number=100, globals=globals()))  # 0.01369050000000005
print(timeit.timeit('two_func(N_3)', number=100, globals=globals()))  # 0.13193860000000002

# При подсчете суммы как в следующей функции время меняется незначительно
# 0.0012665999999998956
# 0.014020799999999944
# 0.14514289999999996

cProfile.run('two_func(N)')
cProfile.run('two_func(N_2)')
cProfile.run('two_func(N_3)')


#       904 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#      1    0.000    0.000    0.000    0.000 task_1_2.py:47(two_func)
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#    899    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#       10004 function calls in 0.004 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#      1    0.002    0.002    0.004    0.004 task_1_2.py:47(two_func)
#      1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#   9999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def three_func(n):
    array = [1 / (-2)**i for i in range(n)]
    sum_ = 0
    for num in array:
        sum_ += num
    return sum_


print(timeit.timeit('three_func(N)', number=100, globals=globals()))  # 0.0064110000000000555
print(timeit.timeit('three_func(N_2)', number=100, globals=globals()))  # 0.10091089999999991
print(timeit.timeit('three_func(N_3)', number=100, globals=globals()))  # 9.2794422

cProfile.run('three_func(N)')
cProfile.run('three_func(N_2)')
cProfile.run('three_func(N_3)')


#       5 function calls in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#      1    0.000    0.000    0.001    0.001 task_1_2.py:88(three_func)
#      1    0.001    0.001    0.001    0.001 task_1_2.py:89(<listcomp>)
#      1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#       5 function calls in 0.093 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.093    0.093 <string>:1(<module>)
#      1    0.000    0.000    0.093    0.093 task_1_2.py:88(three_func)
#      1    0.093    0.093    0.093    0.093 task_1_2.py:89(<listcomp>)
#      1    0.000    0.000    0.093    0.093 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


'''
Вывод: В первом случае даже невозможен подсчет при больших значениях, а также из-за рекурсии происходит долгий расчет.
Но хуже append может быть генератор списка, из-за него увеличивается время работы, поэтому приоритетнее 2 способ.
'''