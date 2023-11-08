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
    size = len(arr)
    stack = [0] * size
    top = -1

    top += 1
    stack[top] = 0
    top += 1
    stack[top] = size - 1

    while top >= 0:
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1

        pivot_index = partition(arr, l, h)

        if pivot_index - 1 > l:
            top += 1
            stack[top] = l
            top += 1
            stack[top] = pivot_index - 1

        if pivot_index + 1 < h:
            top += 1
            stack[top] = pivot_index + 1
            top += 1
            stack[top] = h

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
