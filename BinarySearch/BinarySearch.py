def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    # Check if the array is sorted before performing binary search
    if arr != sorted(arr):
        raise ValueError("Array must be sorted for binary search.")
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

try:
    arr = list(map(int, input("Enter a sorted array of integers (separated by space): ").split()))
    target = int(input("Enter the target element to search for: "))

    # Perform binary search
    result = binary_search(arr, target)

    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found in the array.")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
