# Binary Search Algorithm in Python

## Overview
This repository contains a simple implementation of the Binary Search Algorithm in Python. Binary search is an efficient algorithm used to find the position of a target value within a sorted list. The search works by repeatedly dividing the list in half, checking if the middle element is the target, and then narrowing down the search range accordingly.

## Time Complexity
- Best case: O(1) - The target value is found at the middle position on the first comparison.
- Average case and Worst case: O(log n) - The list is divided in half repeatedly until the target is found or all elements are checked. This logarithmic time complexity makes binary search much more efficient than linear search, especially for large datasets.

## How Binary Search Works:

### Input: 
A sorted list of numbers and a target value to search for.
### Process: 
The algorithm compares the middle element of the list with the target:
- If the middle element is equal to the target, the search is successful.
- If the target is smaller, the search continues in the left half of the list.
- If the target is larger, the search continues in the right half of the list. This process repeats until the target is found or the range of possible elements is exhausted.

### Output: 
If the target value is found, the program prints its position. Otherwise, it indicates that the number was not found.

## Key Features:
- Input Handling: 
The program prompts the user to input a sorted list of integers and the target value to search for.
Efficient Searching: 
- Binary search splits the list in half at each step, drastically reducing the number of comparisons compared to linear search.
- Error Handling: The program checks for invalid inputs and handles exceptions like entering non-integer values.
- Clean Output: If the target is found, the program displays the position using a 0-based index. If not found, it indicates that the target does not exist in the list.

## Example
### Input:
- Enter a sorted array of integers (separated by space): 5 10 15 20 25 30 35 40 45 50
- Enter the target element to search for: 25

### Output:
- Element 25 found at index 4.

### Input (when the element is not found):
- Enter a sorted array of integers (separated by space): 2 4 6 8 10
- Enter the target element to search for: 7

### Output:
- Element 7 not found in the array.

## Enhancements from Original Code
This implementation improves upon the typical binary search by:

- Error Handling: The code includes exception handling to manage invalid user inputs like non-integer values, ensuring the program does not crash unexpectedly.
- Code Simplicity: The search logic is streamlined, making it easier to follow and reducing potential errors.
- Input Validation: Users are reminded to input a sorted list, and a check can be added to enforce this rule, improving reliability.

## How to Run
- Clone the repository: 
1. ``git clone https://github.com/yourusername/binary-search-python.git``
2. ``cd binary-search-python``

## Run the Python script:
1. ``python3 binary_search.py``

### Contributing
Contributions are welcome! If you'd like to improve the implementation or suggest a new feature, follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -m 'Add new feature').
4. Push to your branch (git push origin feature-branch).
5. Open a pull request.

### License
This project is licensed under the ``MIT License`` - see the LICENSE file for details.
