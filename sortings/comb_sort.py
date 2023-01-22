#Worst-case: O(n^2)
#Best-case: O(log(n)*n)

def comb_sort(array):
    length = len(array)
    size = length
    while size > 1:
        size = int(size/1.247)
        for j in range(0, length - size):
            if array[j] > array[j + size]:
                array[j], array[j + size] = array[j + size], array[j]

