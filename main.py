import time
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from heap_sort import heap_sort
from radix_sort import radix_sort

# Example arrays for comparing sorting algorithm performance:
# Small arrays (100 elements):
positive_small_array = [i for i in range (1, 101)] # Positive integers
negative_small_array = [i for i in range (-100, 0)] # Negative integers
mixed_small_array = [i for i in range (-50, 51)] # Positive and negative integers

# Medium arrays (1,000 elements):
positive_medium_array = [i for i in range(1, 1001)] # Positive integers
negative_medium_array = [i for i in range(-1000, 0)] # Negative integers
mixed_medium_array = [i for i in range(-500, 501)] # Positive and negative integers

# Large arrays (10,000 elements):
positive_large_array = [i for i in range(1, 10001)] # Positive integers
negative_large_array = [i for i in range(-10000, 0)] # Negative integers
mixed_large_array = [i for i in range(-5000, 5001)] # Positive and negative integers

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

# Test and measure the performance of sorting algorithm implementations
for algorithm_name, sorting_algorithm in sorting_algorithms.items():
    print(f"Testing {algorithm_name}...")
    arrays = [positive_small_array, negative_small_array, mixed_small_array,
            positive_medium_array, negative_medium_array, mixed_medium_array,
            positive_large_array, negative_large_array, mixed_large_array]

    # Test each array and measure the execution time
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
