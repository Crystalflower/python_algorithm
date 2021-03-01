user_answer = int(input('Введите натуральное число для вывода его отражения: '))
DEFAULT_NUM_FOR_DIVISION = 10


def func(number):
    if number < DEFAULT_NUM_FOR_DIVISION:
        return f'{number}'
    return f'{number % DEFAULT_NUM_FOR_DIVISION}{func(number // DEFAULT_NUM_FOR_DIVISION)}'


print(int(func(user_answer)))
