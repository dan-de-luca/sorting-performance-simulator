def insertion_sort(arr):
    """
    Sorts an array in ascending order using the insertion sort algorithm.

    Args:
        arr (list): The list to be sorted.

    Returns:
        list: The sorted list.

    """
    for i in range(1, len(arr)):
        key = arr[i]  # Select the current element to be inserted
        j = i - 1  # Set the index of the previous element
        while j >= 0 and key < arr[j]:  # Compare the current element with the previous elements
            arr[j + 1] = arr[j]  # Shift the previous element to the right
            j -= 1  # Move to the next previous element
        arr[j + 1] = key  # Insert the current element in its correct position
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
