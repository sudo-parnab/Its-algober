# Two-Pointer Algorithm in Python

## Overview
This repository contains a Python-based implementation of the "two-sum" algorithm, which checks if any two numbers in a list add up to a given target value. The approach is simple and efficient for small datasets, utilizing sorting and a two-pointer technique to optimize performance.

## Time Complexity
- **Best Case**: O(1) - The target pair is found on the first try.
- **Average/Worst Case**: O(n log n) - Sorting the list requires `O(n log n)`, and the search through the list using the two-pointer approach is `O(n)`. This makes the algorithm efficient for mid-sized lists, though it may be slower for very large datasets compared to specialized search algorithms.

## How the Two-Sum Algorithm Works
- **Input**: The program takes in a list of numbers and a target sum. Users provide the input directly in the console.
- **Process**:
  1. The list is sorted to enable the two-pointer method.
  2. Pointers start at both ends of the sorted list and move toward each other. If the sum of the numbers is too low, the left pointer moves right; if too high, the right pointer moves left.
  3. The pointers continue moving until a pair is found or they meet without finding a match.
- **Output**: The program outputs `true` if a pair with the desired sum is found and `false` otherwise.

## Key Features
- **User Input Handling**: Users can input any list and target value directly in the console, making it easy to test with various values.
- **Optimized Search**: Sorting combined with the two-pointer technique reduces the need for an exhaustive search through every possible pair.
- **Boolean Output**: The program outputs a straightforward boolean response (`true` or `false`), making it easy to interpret results without additional details.

## Example Usage
1. **When a Match is Found**  
   - **Input**:  
     - List: `0, -1, 2, -3, 1`
     - Target: `-2`
   - **Output**:  
     - `"true"` because `-3` and `1` sum to `-2`

2. **When No Match is Found**  
   - **Input**:  
     - List: `5, 6, 7`
     - Target: `10`
   - **Output**:  
     - `"false"` since no two numbers add up to 10

## Enhancements
This implementation improves upon basic solutions by:
- **Efficient Pair Search**: Using sorting and two pointers, it finds matches quickly without needing to test every possible pair.
- **Clear Output**: The result is a simple "true" or "false," keeping the output clean and clear.

## How to Run
To use this code:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/two-sum-python.git
