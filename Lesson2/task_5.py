END_COUNT = 9

code = 32
count = 0
while code != 128:
    a = f'{code}: {chr(code)}, '
    if count == END_COUNT:
        print(a, end='\n')
        count = 0
    else:
        print(a, end='')
        code += 1
        count += 1
