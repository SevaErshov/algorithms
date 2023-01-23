#Average-case: O(nlog(n))
#Worst-case: O(n^2)

def partition(array, low, high):
    pivot = array[(low + high) // 2]
    l = low - 1
    r = high + 1

    while True:
        l += 1
        while array[l] < pivot:
            l += 1

        r -= 1
        while array[r] > pivot:
            r -= 1

        if l >= r:
            return r

        array[r], array[l] = array[l], array[r]


def quick_sort(array):

    def _quick_sort(array, low, high):
        if low < high:
            split_index = partition(array, low, high)
            _quick_sort(array, low, split_index)
            _quick_sort(array, split_index + 1, high)

    _quick_sort(array, 0, len(array) - 1)

