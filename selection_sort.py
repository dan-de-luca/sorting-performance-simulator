def selection_sort(arr):
    """
    Sorts an array in ascending order using the selection sort algorithm.

    Args:
        arr (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    for i in range(len(arr)):
        # Assume the current element is the minimum value
        min_index = i
        # Check the rest of the array to see if there is a smaller element
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                # If a smaller element is found, update the minimum index
                min_index = j
        # Swap the current element with the minimum element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
