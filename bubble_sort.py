def bubble_sort(arr):
    """
    Sorts the given array using bubble sort algorithm.

    Args:
        arr (list): The list to be sorted.

    Returns:
        list: The sorted list.

    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
