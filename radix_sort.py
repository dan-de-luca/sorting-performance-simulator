def counting_sort(arr, exp):
    """
    This function performs counting sort on the given array based on the given exponent.

    Args:
    - arr: list of integers to be sorted
    - exp: exponent to be used for sorting

    Returns:
    - None (the input array is sorted in place)
    """
    output = [0] * len(arr)
    count = [0] * 10

    # Count the occurrences of each digit in the input array
    for i in range(len(arr)):
        index = arr[i] // exp
        count[index % 10] += 1

    # Calculate the cumulative count of each digit
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array by placing each element in its correct sorted position
    i = len(arr) - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the sorted output array back to the input array
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
