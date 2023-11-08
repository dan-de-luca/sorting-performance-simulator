import time
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heap_sort
from radix_sort import radix_sort

# Example arrays
small_array_1 = [5, 2, 9, 1, 5]
small_array_2 = [3, 1]
small_array_3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

medium_array_1 = [38, 27, 43, 3, 9, 82, 10, 19, 42, 55]
medium_array_2 = [64, 34, 25, 12, 22, 11, 90, 87, 76, 42, 55, 68]
medium_array_3 = [93, 28, 67, 41, 55, 60, 72, 89, 97, 13, 47, 25, 33]

large_array_1 = [i for i in range(1000, 0, -1)]
large_array_2 = [i for i in range(1, 10001)]
large_array_3 = [i for i in range(10000, 0, -1)]

# Sorting algorithms to test
sorting_algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort,
    "Radix Sort": radix_sort
}

# Test and measure the performance of sorting algorithms
for algorithm_name, sorting_algorithm in sorting_algorithms.items():
    print(f"Testing {algorithm_name}...")
    arrays = [small_array_1, small_array_2, small_array_3,
            medium_array_1, medium_array_2, medium_array_3,
            large_array_1, large_array_2, large_array_3]

    total_time = 0
    for idx, array in enumerate(arrays):
        start_time = time.time()
        sorting_algorithm(array.copy())
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Array {idx + 1} of size {len(array)} sorted in {execution_time:.6f} seconds.")
        total_time += execution_time

    average_time = total_time / len(arrays)
    print(f"Average time for {algorithm_name}: {average_time:.6f} seconds.\n")
