# Recursive approach (may hit recursion limit)
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0]
#         less = [x for x in arr[1:] if x <= pivot]
#         greater = [x for x in arr[1:] if x > pivot]
#         return quick_sort(less) + [pivot] + quick_sort(greater)

# Iterative approach (using stack)
def quick_sort(arr):
    """
    Sorts the input array using the iterative quick sort algorithm.

    Args:
        arr (list): The input list to be sorted.

    Returns:
        list: The sorted list.

    """
    size = len(arr)
    stack = [0] * size
    top = -1

    top += 1
    stack[top] = 0
    top += 1
    stack[top] = size - 1

    while top >= 0:
        # Pop the topmost values from the stack
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        # Partition the array around the pivot element
        pivot_index = partition(arr, l, h)

        # If there are elements on the left side of the pivot,
        # push the left indices to the stack
        if pivot_index - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = pivot_index - 1

        # If there are elements on the right side of the pivot,
        # push the right indices to the stack
        if pivot_index + 1 < h:
            top += 1
            stack[top] = pivot_index + 1
            top += 1
            stack[top] = h

    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
