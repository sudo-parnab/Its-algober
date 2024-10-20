# Stack Data Structure Implementation in Python

## Overview
This repository contains a simple implementation of the Stack Data Structure in Python using Linked List. The stack data structure is a linear data structure that follows the principle of Last In First Out (The last element inserted is the first to be popped out). Its basic operations are as follows:

* push() to insert an element into the stack.
* pop() to remove an element from the stack.
* isEmpty() returns true if stack is empty else false.
* peek() Returns the top element of the stack.


## Time Complexity of Operations
- push(): O(1) 
- pop(): O(1)
- isEmpty(): O(1)
- peek(): O(1)

## How Stack Implementation Works:

### Input:

- A choice of operation from the above choices.

### Process: 

- The choice made by the user indicates which operation to perform. They are as follows:

1. push(data): 
    - It creates a new Node with the given data.
    - Sets the new node's next to the current root (linking it to the previous top).
    - Updates root to point to the new node (making it the new top).

2. pop():
    - First, it checks if the stack is empty using isEmpty().
    - If not empty, it stores the current root in a temporary variable.
    - Updates root to point to the next node (new top).
    - Returns and prints the data from the removed top node.

3. isEmpty():
    - It simply checks if the root (top of the stack) is None. If so, the stack is empty.

4. peek():
    - Checks if the stack is empty.
    - If not empty, it simply accesses and prints the data of the root node without modifying the stack.

### Output: 

- If the operation choice is any number between 0 and 5 (exclusive bounds), the program performs the corresponding operation and offers the choice to the user again. Otherwise, it indicates that the exit operation was triggered and ends the program.

## Key Features:

- Input Handling: 
    - The program prompts the user to input a choice of operation.
- Error Handling: 
    - The program checks for invalid inputs and handles exceptions like entering non-integer values.
- Clean Output: 
    - In the case of the pop and peek functions, if the top element exists, it returns its value. If not found, it indicates that the top element does not exist.

## Example
### Input 1 (Push operation):
```bash
*********** Stack Operations ***********
Choose from the following operations:
1. Push Element
2. Pop Element
3. Check If Stack Empty
4. Peek Top Element
Enter any other value to exit

Choose an operation: 1
Enter the value to be pushed: 20
```

### Output 1:
```bash
20 pushed to stack
```

### Input 2 (Peek operation after Input 1):
```bash
Choose the next operation: 4
```

### Output 2:
```bash
Top element is 20
```

### Input 3 (isEmpty operation after Input 2):
```bash
Choose the next operation: 3
```

### Output 3:
```bash
There are elements in the stack currently.
```

### Input 4 (Pop operation after Input 3):
```bash
Choose the next operation: 2
```

### Output 4:
```bash
20 popped from stack
```

### Input 5 (Peek operation after Input 4):
```bash
Choose the next operation: 4
```

### Output 5:
```bash
No elements in the stack
```

### Input 6 (Pop operation after Input 5):
```bash
Choose the next operation: 2
```

### Output 6:
```bash
No elements in the stack
```

### Input 7 (isEmpty operation after Input 6):
```bash
Choose the next operation: 3
```

### Output 7:
```bash
There are no elements in the stack currently.
```

### Input 8 (Non-numeric Input Given):
```bash
Choose the next operation: p
```

### Output 8:
```bash
Exit Operation Triggered...
```

## Enhancements from Original Code
- This implementation improves upon the typical stack implementation by:
    - Error Handling: The code includes exception handling to manage invalid user inputs like non-integer values, ensuring the program does not crash unexpectedly.

## How to Run

- Clone the repository: 
    1. ``git clone github.com/<your-username>/<your-repository>.git ``
    2. ``cd PythonDS/Stack``

## Run the Python script:
- Run the following script
    1. ``python3 Stack.py``

### Contributing
Contributions are welcome! If you'd like to improve the implementation or suggest a new feature, follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -m 'Add new feature').
4. Push to your branch (git push origin feature-branch).
5. Open a pull request.

### License
This project is licensed under the ``MIT License`` - see the LICENSE file for details.
