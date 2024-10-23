## Insertion Sort

Insertion sort is a simple sorting algorithm that iteratively constructs a sorted section of an array one element at a time. It is an in-place comparison-based method with an average time complexity of O(n2).

The array is divided into two halves by the method: sorted and unsorted. The first element of the array is first considered the sorted component, whereas the remaining items are originally considered the unsorted component.

The algorithm subsequently compares each unsorted element to the elements in the sorted segment, beginning at the end, and adjusts the bigger elements one position to the right until the unsorted element is found in the correct location.

After determining the proper location, the unsorted element is placed into the sorted component at that location.

This procedure is repeated until all of the members of the unsorted part have been inserted into the sorted part, resulting in a fully sorted array.


#### Advantages:
- Easy implementation: Because the approach is simple to build and understand, it is a great option for teaching basic sorting concepts.
- Because it sorts the array in place, insertion sort does not require any additional memory space.
- Insertion sort is an adaptive sorting algorithm that works best with partially sorted input arrays.
- Stable sorting means that the method keeps equal elements in the input array in the same relative order.


#### Disadvantages:
- Slow for large arrays: With an average time complexity of O(n2), the algorithm is slow for large arrays.
- Insertion sort is inefficient for random input arrays because it involves a large number of comparisons and shifts.
- The algorithm is not suited for parallelization since each iteration is dependent on the outcome of the preceding iteration.
