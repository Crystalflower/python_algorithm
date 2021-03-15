# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

import sys

user_answer = int(input('Введите натуральное число для вывода его отражения: '))
DEFAULT_NUM_FOR_DIVISION = 10

first_weight = list()

first_weight.append(sys.getrefcount(user_answer))
first_weight.append(sys.getrefcount(DEFAULT_NUM_FOR_DIVISION))


def func(number):
    if number < DEFAULT_NUM_FOR_DIVISION:
        return f'{number}'
    first_weight.append(sys.getrefcount(number))
    return f'{number % DEFAULT_NUM_FOR_DIVISION}{func(number // DEFAULT_NUM_FOR_DIVISION)}'


print(int(func(user_answer)))
print(sum(first_weight))  # 42


##############################################################################################

second_weight = list()

user_answer = input('Введите натуральное число для вывода его отражения: ')
second_weight.append(sys.getrefcount(user_answer))

print(int(user_answer[::-1]))

print(sum(second_weight))  # 2

##############################################################################################

third_weight = list()

user_answer = list(input('Введите натуральное число для вывода его отражения: '))
third_weight.append(sys.getrefcount(user_answer))

user_answer.reverse()
result = ''.join(user_answer)

third_weight.append(sys.getrefcount(result))

print(int(result))
print(sum(third_weight))  # 4

'''
Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32

Вывод: Больше всего памяти использует первый - рекурсивный метод, если расматривать с переприсваиванием переменных, 
а также для него необходимо константное значение делителя.
Второй метод характеризуится наименьшим показателем, так как работа происходит только с одной переменной.

'''