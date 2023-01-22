#O(n^2)


def bubble_sort(array):
    length = len(array)
    for i in range(length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

#Если j > j + 1 элемент, то мы меняем их местами. При каждой итерации цикла с i вверх поднимается один элемент. Таким образом, последние i элементов мы уже не трогаем. 
#Улучшенная версия: проверяем, не подан ли нам на вход уже отсортированный массив

def bubble_sort(array):
    length = len(array)
    swapped = False
    for i in range(length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if swapped:
            return
