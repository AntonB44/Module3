'''Самостоятельная работа по уроку "Рекурсия"
Цель: применить знания о рекурсии в решении задачи.
Пишем решение согласно рекомендуемому алгоритму:'''

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
result1 = get_multiplied_digits(304)
result2 = get_multiplied_digits(340)
print(result)
print(result1)
print(result2)

print('При тестировании обнаружилось, что если передать в функцию')
print('число, оканчивающееся на 0, то в результате будет 0.')
print('Так и задумывалось или нужно доработать?')
