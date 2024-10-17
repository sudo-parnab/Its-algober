numbers = []
found = False
number_of_values = int(input("Enter the number of values to enter: "))

# Taking input and appending to the list
for i in range(number_of_values):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

# Input the value to search for
search_value = int(input("Enter a number to search for: "))

# Linear search with enumerate
for index, number in enumerate(numbers):
    if number == search_value:
        found = True
        break

# Result
if found:
    print(f"{search_value} found at position {index + 1}")
else:
    print("Number not found")
