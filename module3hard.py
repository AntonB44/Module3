'''А есть ли универсальное решение для подсчёта суммы всех чисел
 и длин всех строк?

 В данной задаче самым на мой взгляд, сложным моментом является разный механизм доступа
 к элементам словарей, списков, множеств, строк, целых и дробных чисел.
 А механизм рекурсивного вызова функции здесь подходит как нельзя лучше.
 Поскольку был применен рекурсивный вызов функции, на конечном этапе должен быть один входной
 параметр, и поэтому у функции по определению должен быть один параметр, а не *args?
 Или я не прав?
 Во всяком случае с параметром *args при выполнении возникала ошибка переполнения количества
 вызовов рекурсивной функции'''


def calculate_structure_sum(x):
    sum_1 = 0
    if isinstance(x, dict):
        for key, value in x.items():
            sum_1 += calculate_structure_sum(key)
            sum_1 += calculate_structure_sum(value)
    elif isinstance(x, (list, tuple, set)):
        for item in x:
            sum_1 += calculate_structure_sum(item)
    elif isinstance(x, str):
        sum_1 += len(x)
    elif isinstance(x, (int, float)):
        sum_1 += x
    return sum_1


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)

