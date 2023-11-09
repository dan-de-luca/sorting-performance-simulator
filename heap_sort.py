def heapify(arr, n, i):
    """
    Heapify subtree rooted at index i.
    :param arr: List of integers
    :param n: Size of heap
    :param i: Index of root node
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # If left child is larger than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # If right child is larger than largest so far
    if right < n and arr[largest] < arr[right]:
        largest = right

    # If largest is not root
    if largest != i:
        # Swap root with largest
        arr[i], arr[largest] = arr[largest], arr[i]
        # Heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
