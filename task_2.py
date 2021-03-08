# 2). Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

import timeit
import cProfile

I_1 = 10
I_2 = 100
I_3 = 1000


def one_func(n):
    a = [0] * n**2  # создание массива с n количеством элементов
    for i in range(n**2):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n**2:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < n**2:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
        if len(b) == n:
            break

    del a
    return b[n-1]


# print(timeit.timeit('one_func(I_1)', number=100, globals=globals()))  # 0.007348599999999997
# print(timeit.timeit('one_func(I_2)', number=100, globals=globals()))  # 0.9650622999999999
# print(timeit.timeit('one_func(I_3)', number=100, globals=globals()))  # 123.5937004

cProfile.run('one_func(I_1)')
cProfile.run('one_func(I_2)')
cProfile.run('one_func(I_3)')

#       8924 function calls in 1.315 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    1.315    1.315 <string>:1(<module>)
#      1    1.314    1.314    1.315    1.315 task_2.py:20(one_func)
#      1    0.000    0.000    1.315    1.315 {built-in method builtins.exec}
#   7920    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#   1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def two_func(i):
    start = 2
    simple_num = []
    while len(simple_num) != i:
        if simple_num:
            simple = True
            for j in simple_num:
                if start % j == 0:
                    simple = False
                    break
            if simple:
                simple_num.append(start)
        else:
            simple_num.append(start)
        start += 1
    return simple_num[-1]


print(timeit.timeit('two_func(I_1)', number=100, globals=globals()))  # 0.0011957000000000217
print(timeit.timeit('two_func(I_2)', number=100, globals=globals()))  # 0.028992899999999988
print(timeit.timeit('two_func(I_3)', number=100, globals=globals()))  # 2.2385745

cProfile.run('two_func(I_1)')
cProfile.run('two_func(I_2)')
cProfile.run('two_func(I_3)')

#       8923 function calls in 0.024 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.024    0.024 <string>:1(<module>)
#      1    0.023    0.023    0.024    0.024 task_2.py:59(two_func)
#      1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
#   7919    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#   1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
Вывод: Скорее всего я не поняла метод решета и получилась такая костыльная реализация. 
Пыталась узнать промежуток всех чисел(через зависимость), которые включают n простых, 
но тогда верхняя граница и будет искомым числом. 
И тогда нужно было бы дополнять первоначальный список с нулями, пока во втором не будет искомого, 
но это противоречит методу.
Написать свой код оказалось намного проще.

P.S. Приводить сравнение пока бессмысленно :(
Комментарии из методички оставила чтобы не запутаться.
'''