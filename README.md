# sorting-performance-simulator

Simulation & performance comparison of basic implementations of the following commonly used sorting algorithms:
- **Bubble Sort:** Bubble sort compares adjacent elements in an array & swaps them if they are not in order (ascending). This process is repeated until the array is sorted.
  Bubble sort is simple to understand & implement, however it is inefficient for large datasets. Complexity - Time: Worst-case & Avg.-case = O(n^2), Best-case = O(n). Bubble
  sort is an in-place sorting algorithm. Space: O(1)).
- **Insertion Sort:** Insertion sort builds the final sorted array one element at a time, inserting each element into the correct (sorted) position. Insertion sort is equal
  (generally) in complexity (time & space) to bubble sort & selection sort.
- **Selection Sort:** Selection sort divides the input array into two parts: a sorted & an unsorted sub-array. It then repeatedly selects the smallest (or largest, depending
  on required order) element from the unsorted sub-array & moves it to the sorted sub-array. Complexity: Selection sort is equal (generally) in complexity (time & space) to
  bubble sort & insertion sort.
- **Merge Sort:** Merge sort is a divide-&-conquer sorting algorithm that divides the unsorted array into n sub-arrays, each containing a single element. Each sub-array is then
  merged in the desired order, producing a single sorted array. Complexity - Time: Worst, Avg. & Best-case = O(n log n), Space: O(n) as merge sort requires additional space for
  merging).
- **Quick Sort:** Quick sort is another divide-&-conquer sorting algorithm that uses a selected 'pivot' element to partition the remaining array elements into two sub-arrays, one
  containing all elements smaller than the pivot element, & the other containing all elements larger than the pivot element. The sub-arrays are then sorted recursively & joined to
  produce the final sorted array. Complexity - Time: Worst-case = O(n^2) in the rare (generally) case of unbalanced pivot selection), Avg.-case = O(n log n), Best-case = O(n log n)
  when the pivot selection is balanced. Space: O(log n) to O(n) depending on the implementation (recursion vs. stack optimisation).
- **Heap Sort:** Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure. The array elements are divided into sorted & unsorted regions, then
  the unsorted regions is iteratively shrunk by extracting the largest (or smallest, depending on the desired final order) element & moving it to the sorted region.
  Complexity - Time: Worst, Avg. & Best-case = O(n log n), Space: O(1) (in-place sorting).
- **Radix Sort:** Radix sort is a non-comparitive sorting algorithm that sorts numbers by processing individual digits from least-significant (LSD) to most-significant (MSD) or
  vice versa depending on the desired final order. Complexity - Time: Worst, Avg. & Best-case = O(nk), Space: O(n + k) as radix sort requires additional space for counting & ouput
  arrays, where k is the number of digits.

# Inputs

Sorting algorithm performance is compared using several small, medium & large arrays as input.

# Performance

Sorting algorithm performance is measured in seconds.
