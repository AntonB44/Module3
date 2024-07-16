'''омашняя работа по уроку "Пространство имён"
Цель: применить на практике начальные знания о пространстве имён и оператор global.
Закрепить навыки из предыдущих модулей.

Задача "Счётчик вызовов"'''
calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    list_return = [len(string), string.lower(), string.upper()]
    count_calls()
    return list_return
def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search_l = [x.lower() for x in list_to_search]# переводим все элементы входного списка в нижний регистр
    if string in list_to_search_l:
        contain_flag = True
    else:
        contain_flag = False
    return contain_flag


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

print(string_info('Я изучаю Питон'))
print(is_contains('Никто', ['Кто', 'нибудь', 'Знает']))
print(is_contains('кто-то', ['Может', 'КТО-ТО', 'И Знает']))
print(calls)

