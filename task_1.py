# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

import collections

Company = collections.namedtuple(
    'Company',
    'name, first_quarter, second_quarter, third_quarter, fourth_quarter, average_profit'
)

count_comp = int(
    input('Введите количество предприятий для составления отчета по прибыли за год (положительное число): ')
)

i = 1

all_company = []
all_sum_average = 0

while i <= count_comp:
    name_comp = input(f'Введите название {i} предприятия: ')
    first_quarter = int(input('Введите прибыль за первый квартал: '))
    second_quarter = int(input('Введите прибыль за второй квартал: '))
    third_quarter = int(input('Введите прибыль за третий квартал: '))
    fourth_quarter = int(input('Введите прибыль за четвертый квартал: '))
    average_profit = first_quarter + second_quarter + third_quarter + fourth_quarter

    comp = Company(name_comp, first_quarter, second_quarter, third_quarter, third_quarter, average_profit)
    all_company.append(comp)

    all_sum_average += average_profit
    i += 1

average_companies = all_sum_average / count_comp
highest_average = []
lowest_average = []


for company in all_company:
    if company.average_profit > average_companies:
        highest_average.append(company.name)
    elif company.average_profit < average_companies:
        lowest_average.append(company.name)

print(f'Средняя прибыль компаний - {round(average_companies)}!')

if highest_average:
    print('Компании с доходом выше среднего: ')
    for i in highest_average:
        print(i)

    print('Компании с доходом ниже среднего: ')
    for i in lowest_average:
        print(i)
else:
    print('У всех одинаковый доход!')
