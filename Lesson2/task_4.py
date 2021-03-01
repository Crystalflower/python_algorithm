DEFAULT_START_NUM = -2
DEFAULT_START_SUMMA = 0

user_answer = int(input('Введите количество элементов для расчета суммы их последовательности (до 997): '))


def func(count, start_num, sum):
    result = start_num / -2
    count -= 1
    sum += result
    if count == 0:
        return f'{result}\nСумма последовательности: {sum}'
    return f'{result}, {func(count, result, sum)}'


print(func(user_answer, DEFAULT_START_NUM, DEFAULT_START_SUMMA))
