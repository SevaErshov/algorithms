#O(nlog(n))

def merge_sort(array):
    if len(array) <= 1:
        return array
    split_index = len(array) // 2
    left = array[:split_index]
    right = array[split_index:]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    left_length = len(left_sorted)
    right_length = len(right_sorted)
    sum_length = left_length + right_length
    output_array = [0] * sum_length

    i = 0
    j = 0
    for k in range(sum_length):
        if i >= left_length:
            output_array[k] = right_sorted[j]
            j += 1
            continue

        if j >= right_length:
            output_array[k] = left_sorted[i]
            i += 1
            continue

        if left_sorted[i] > right_sorted[j]:
            output_array[k] = right_sorted[j]
            j += 1

        else:
            output_array[k] = left_sorted[i]
            i += 1

    return output_array


