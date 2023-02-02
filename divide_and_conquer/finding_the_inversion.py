#O(nlog(n))

def count_inversions(array):
    """
    params: array
    return: sorted array and number of inversions
    """
    if len(array) == 0 or len(array) == 1:
        return array, 0

    split_index = len(array) // 2
    left = count_inversions(array[:split_index])
    right = count_inversions(array[split_index:])
    left, left_count = left[0], left[1]
    right, right_count = right[0], right[1]

    return merge_and_count(left, right, left_count + right_count)

def merge_and_count(left, right, count):
    i, j = 0, 0
    output = list()
    for k in range(len(right) + len(left)):
        if i >= len(left):
            output.extend(right[j:])
            return output, count
        elif j >= len(right):
            output.extend(left[i:])
            return output, count

        if left[i] <= right[j]:
            output.append(left[i])
            i += 1
        else:
            count += len(left) - i
            output.append(right[j])
            j += 1

    return output, count

