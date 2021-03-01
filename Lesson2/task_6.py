from random import randrange

hidden_number = randrange(0, 101)
count_attempt = 10

print('Вас приветствует игра угадайка! У вас 10 попыток.')
while count_attempt > 0:
    user_answer = int(input('Введите число, которое мог загадать компьютер от 1 до 100: '))
    if user_answer == hidden_number:
        print('Поздравляю, вы угадали!')
        break
    elif user_answer > hidden_number:
        count_attempt -= 1
        print(f'Ответ не верный, число меньше. У вас осталось {count_attempt} попыток')
    else:
        count_attempt -= 1
        print(f'Ответ не верный, число больше. У вас осталось {count_attempt} попыток')


if count_attempt == 0:
    print(f'Вы проиграли :(\nПравильный ответ - {hidden_number}')
