#O(n + k)

def counting_sort(array, length):
    """
    input: a collection of objects according to keys that are small positive integers
    length - max number in array (if length = 100, it means that a collection is {1, 2, 3, ..., 98, 99, 100}
    """
    memory = dict()
    
    for num in array:
        memory[num] = memory.get(num, 0) + 1

    output = [0] * len(array)
    b = 0
    for k in range(length + 1):
        for i in range(memory.get(k, 0)):
            output[b] = k
            b += 1

    return output


