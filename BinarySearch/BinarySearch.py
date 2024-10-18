def binary_search(arr, target):
    # Type checking
    if not isinstance(target, int):
        raise TypeError("Target must be an integer.")
    if not all(isinstance(item, int) for item in arr):
        raise TypeError("Array must contain only integers.")
    
    # Sort validation
    if arr != sorted(arr):
        raise ValueError("Array must be sorted before performing binary search.")

    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Check if the middle element is the target
        if arr[mid] == target:
            return mid
        
        # If target is greater, ignore the left half
        elif arr[mid] < target:
            left = mid + 1
            
        # If target is smaller, ignore the right half
        else:
            right = mid - 1
    
    # If target is not present in the array
    return -1

# Input section
try:
    arr = list(map(int, input("Enter a sorted array of integers (separated by space): ").split()))
    target = int(input("Enter the target element to search for: "))

    # Perform binary search
    result = binary_search(arr, target)

    # Output the result
    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in the array.")
except ValueError as ve:
    print(f"Invalid input: {ve}")
except TypeError as te:
    print(te)
except ValueError as ve:
    print(ve)
