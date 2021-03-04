# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

START_DIVIDER_AND_DIVIDEND = 2
END_DIVIDER = 10
END_DIVIDEND = 100


result = {x: 0 for x in range(START_DIVIDER_AND_DIVIDEND, END_DIVIDER)}

for dividend in range(START_DIVIDER_AND_DIVIDEND, END_DIVIDEND):
    for divider in range(START_DIVIDER_AND_DIVIDEND, END_DIVIDER):
        if dividend % divider == 0:
            result[divider] += 1

for i, j in result.items():
    print(i, j)
