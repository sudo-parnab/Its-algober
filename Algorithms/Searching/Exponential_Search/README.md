# Two-Pointer Search Module

## Overview
The **Two-Pointer Search Module** provides efficient algorithms for searching specific elements within sorted arrays using a two-pointer approach. This technique leverages two indices that move towards each other to optimize search efficiency, particularly when array sorting allows for reduced search space. This method is commonly used to find pairs that meet certain criteria, such as summing to a target value.

## Why Use Two-Pointer Search?
The two-pointer technique simplifies the search for elements that satisfy a condition in sorted arrays by reducing time complexity compared to traditional methods. It provides a straightforward, efficient way to:
- Find pairs or combinations of elements in sorted arrays.
- Improve the efficiency of target-based searches with reduced complexity.
- Perform in-place searches without additional data structures.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
  - [Searching for a Pair](#searching-for-a-pair)
  - [Setting Custom Conditions](#setting-custom-conditions)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## Features
- Efficiently locate elements or pairs in sorted arrays that meet specified criteria.
- Minimal and intuitive interface for easy integration.
- Comprehensive error handling for common input issues.

## Getting Started
### Prerequisites
To use this module, you need **C++** with a **C++11 or later compatible compiler**.

## Installation
1. Download the `two_pointer_search.cpp` file from this repository.
2. Integrate it into your C++ project or compile it independently.

## Usage
The module provides functionalities to search for a target element and to check for element pairs that meet specific conditions.

### Searching for a Pair
The `two_sum` function accepts a sorted array and a target sum, returning `true` if two elements in the array add up to the target.

```cpp
#include "two_pointer_search.h"  // Include your module header

std::vector<int> arr = {1, 2, 4, 6, 10};
int target = 10;

// Example: Find if there is a pair that sums to the target
bool result = two_sum(arr, target);
std::cout << "Pair found: " << std::boolalpha << result << std::endl;
