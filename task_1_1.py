# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

import sys

DEFAULT_START_NUM = -2
DEFAULT_START_SUMMA = 0

N = 100

first_weight = list()

first_weight.append(sys.getsizeof(DEFAULT_START_NUM))
first_weight.append(sys.getsizeof(DEFAULT_START_SUMMA))
first_weight.append(sys.getsizeof(N))


def one_func(count, start_num, sum_):
    result = start_num / -2
    count -= 1
    sum_ += result

    first_weight.append(sys.getsizeof(result))
    first_weight.append(sys.getsizeof(count))
    first_weight.append(sys.getsizeof(sum_))

    if count == 0:
        return f'{result}\nСумма последовательности: {sum_}'
    return f'{result}, {one_func(count, result, sum_)}'


print(one_func(N, DEFAULT_START_NUM, DEFAULT_START_SUMMA))
print(sum(first_weight))  # 7676

#############################################################################

second_weight = list()

second_weight.append(sys.getsizeof(N))


def two_func(n):
    array = [1]
    for _ in range(n - 1):
        array.append(array[-1] / -2)
    second_weight.append(sys.getsizeof(array))
    return sum(array)


print(two_func(N))
print(sum(second_weight))  # 956

##############################################################################

third_weight = list()

third_weight.append(sys.getsizeof(N))


def three_func(n):
    array = [1 / (-2)**i for i in range(n)]
    sum_ = 0
    for num in array:
        sum_ += num
        third_weight.append(sys.getsizeof(num))
    third_weight.append(sys.getsizeof(array))
    third_weight.append(sys.getsizeof(sum_))
    return sum_


print(three_func(N))
print(sum(third_weight))  # 3364


'''
Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32

Вывод: Так же как и в прошлой задаче больше памяти использует рекурсивный метод. 
Учитывая вывод 4 урока:
"В первом случае даже невозможен подсчет при больших значениях, а также из-за рекурсии происходит долгий расчет.
Но хуже append может быть генератор списка, из-за него увеличивается время работы, поэтому приоритетнее 2 способ."
можно сказать что 2 вариант выигрывает и по использованию памяти. 

'''
