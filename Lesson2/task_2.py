user_answer = int(input('Введите натуральное число для подсчета четных и нечетных чисел в нем: '))
start_even = 0
start_odd = 0
DEFAULT_NUM_FOR_DIVISION = 10


def func(num, even, odd):
    numeral = num % DEFAULT_NUM_FOR_DIVISION
    if num <= 0:
        return f'\nвсего {even} четных, {odd} нечетных'
    if numeral % 2 == 0:
        return f'четная {numeral}, {func(num // DEFAULT_NUM_FOR_DIVISION, even + 1, odd)}'
    else:
        return f'нечетная {numeral}, {func(num // DEFAULT_NUM_FOR_DIVISION, even, odd + 1)}'


result = func(user_answer, start_even, start_odd)

print(f'Результат анализа числа {user_answer}: \n{result}')
