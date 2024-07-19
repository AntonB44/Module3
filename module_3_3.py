'''Домашнее задание по уроку "Распаковка позиционных параметров".

Цель задания: Освоить создание функций с параметрами по умолчанию
и практику вызова этих функций с различным количеством аргументов.'''


def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(2,4)
print_params('a', 'b', 'c')
# print_params(1,2, 3, 4, 5)
'''Поскольку в функции prim_params ипользуются все три параметра по умолчанию,
передача не всех аргументов не приводит к ошибке, но если мы пытаемся передать
большее количество аргументов, будет ошибка (стр 16)'''


values_list = ('mother', False, 1024)
values_dict = {'a' : 3.25, 'b': 'Programm', 'c': False}
print_params(*values_list)
print(values_dict)
print_params(*values_dict)# в этом случае выводятся ключи словаря
print_params(**values_dict)# в этом случае выводятся значения ключей


values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)# при передаче распаковки списка из двух элементов, функция воспринимает 42 как параметр а
