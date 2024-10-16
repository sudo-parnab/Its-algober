def binary_search(arr, target):
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
except ValueError:
    print("Invalid input. Please enter integers only.")
