# Linear Search Algorithm in Python

## Overview
This repository contains a simple implementation of the Linear Search Algorithm in Python. Linear search is a basic algorithm used to search for a target value within a list. The search iterates through each element of the list one by one until the target is found or the list ends.

## Time Complexity
- Best case: O(1) - The target value is found at the first position.
- Worst case: O(n) - The target value is either at the last position or not present in the list at all, requiring the algorithm to traverse the entire list.

This linear time complexity, O(n), makes linear search less efficient than other searching algorithms like binary search for large datasets, but it remains useful for small or unsorted lists.


## How Linear Search Works:
- Input: A list of numbers and a target value to search for.
- Process: The algorithm checks each element of the list sequentially. If the current element matches the target value, the search is successful.
- Output: If the target value is found, the program prints its position. Otherwise, it indicates that the number was not found.



## Key Features:
1. Input Handling:
The program first asks the user for the number of values to input.
Then, it prompts the user to enter each number, which is stored in a list.
2. Efficient List Iteration:
The enumerate() function is used to iterate over the list, providing both the index and the value at each step. This simplifies the process of tracking the current position of each element in the list.
3. Boolean Flag:
A found flag is used to determine whether the target number has been located. If the number is found during iteration, the flag is set to True, and the search ends early to optimize performance.
4. Formatted Output:
The program uses Python f-strings to print the result, making the output clear and easy to understand. It displays the position of the found element in a user-friendly 1-based format (i.e., the first element is in position 1, not 0).

## Example

### Input:

- Enter the number of values to enter: 5
- Enter number 1: 10
- Enter number 2: 20
- Enter number 3: 30
- Enter number 4: 40
- Enter number 5: 50
- Enter a number to search for: 30

### Output:
30 found at position 3

### Input (when the number is not found):

- Enter the number of values to enter: 3
- Enter number 1: 5
- Enter number 2: 15
- Enter number 3: 25
- Enter a number to search for: 10

### Output:
Number not found

## Enhancements from Original Code
This implementation improves upon the original linear search by:

1. Using enumerate(): Reduces code complexity by eliminating the need for a manual index counter.
2. Cleaner Boolean Logic: The comparison if flag == True is replaced with if found, following Python’s best practices for boolean values.
3. User-Friendly Output: The result is printed using formatted strings (f-strings), improving readability and clarity.

## How to Run
### Clone the repository:

- ``git clone https://github.com/yourusername/linear-search-python.git`` 
- ``cd linear-search-python``

### Run the Python script:
python3 ``linear_search.py``

### Contributing
Feel free to contribute by submitting issues, requesting new features, or making improvements. To contribute:
1. Fork the repository.
2. Create a new branch (``git checkout -b feature-branch``).
3. Commit your changes (``git commit -m 'Add a new feature'``).
4. Push to the branch (``git push origin feature-branch``).
5. Open a pull request.

### License
This project is licensed under the ``MIT License`` - see the LICENSE file for details.
