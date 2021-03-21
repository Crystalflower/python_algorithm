# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

from hashlib import md5


def get_substrings(str_val):
    len_str = len(str_val)
    count = []

    for i in range(len_str):
        for j in range(i + 1, len_str + 1):
            val_hash = md5(str_val[i:j].encode('utf-8')).hexdigest()
            if len(str_val[i:j]) == len_str:
                continue
            if val_hash in count:
                continue
            count.append(val_hash)

    return len(count)


user_answer = input('Введите любую строку: ')
a = get_substrings(user_answer)

print(f'Количество подстрок в строке {user_answer} = {a}')
