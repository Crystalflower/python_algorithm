# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

import collections

NUMBERS_SIXTEEN = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
MAX_SIXTEEN_NUMS = 16

first_num = collections.deque(input('Введите первое число в 16 системе счисления для дальнейших операций: '))
second_num = collections.deque(input('Введите второе число в 16 системе счисления для дальнейших операций: '))

len_1 = len(first_num)
len_2 = len(second_num)


def addition(
        lenght,
        frst=None,
        scnd=None,
        added=None,
        rslt=None
):
    for i in range(lenght):
        if frst:
            first = NUMBERS_SIXTEEN.index(frst.pop())
        else:
            first = 0
        if scnd:
            second = NUMBERS_SIXTEEN.index(scnd.pop())
        else:
            second = 0
        if added:
            number_result = first + second + 1
            added = None
        else:
            number_result = first + second
        if number_result >= MAX_SIXTEEN_NUMS:
            number_result -= MAX_SIXTEEN_NUMS
            added = True
        rslt.appendleft(NUMBERS_SIXTEEN[number_result])
    return added


result = collections.deque()
added_one = None

if len_1 == len_2:
    added_one = addition(len_1, first_num, second_num, added_one, result)
elif len_1 > len_2:
    added_one = addition(len_2, first_num, second_num, added_one, result)
    added_one = addition(len_1-len_2, first_num, added=added_one, rslt=result)
else:
    added_one = addition(len_1, first_num, second_num, added_one, result)
    added_one = addition(len_2-len_1, second_num, added=added_one, rslt=result)
if added_one:
    result.appendleft('1')


print(f'Результат сложения: {"".join(result)}')
