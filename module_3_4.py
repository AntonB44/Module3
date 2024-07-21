'''Самостоятельная работа по уроку "Произвольное число параметров".
Цель: закрепить знание использования параметров *args/ **kwargs на практике.'''

'''Реализован следующий алгоритм:
1.Переводим входящие параметры в нижний регистр
2.Объединяем обязательное слово и принимаемый список в один список
3.Ищем в объединенном списке элемент с минимальной длиной
4.Записываем этот элемент в строку root_x
5.Находим во входящем списке все элементы, которые содержат короткий элемент
при условии что он содержится и в обязательном слове
6.Добавляем этот элемент в список same_words.
!!!Обращаю внимание, что в тексте задания в последнем примере не вывелось слово Mable!!!'''

def single_root_words(root_word, *other_words):
    same_words = []
    root_word_l = root_word.lower()
    other_words_l = [x.lower() for x in other_words]
    sum_elements = [root_word_l,]
    list_other_words_l = list(other_words_l)
    sum_elements = sum_elements + list_other_words_l
    root_x_l = len(root_word)
    root_x = root_word_l
    for j in range(len(sum_elements)):
        if len(sum_elements[j]) < root_x_l:
            root_x_l = len(sum_elements[j])
            root_x = sum_elements[j]
    for i in range(len(other_words_l)):
        if root_x in other_words_l[i] and root_x in root_word_l:
            same_words.append(other_words[i])
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)