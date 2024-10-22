# Linked List Data Structure Implementation in Python

## Overview
This repository contains a simple implementation of the Linked List Data Structure in Python. The linked list is a linear data structure that is a collection of nodes that each contain a value as well as the address of the next node in the list. Its basic operations are as follows:

* insertStart() to insert a node at the start of the linked list
* insertEnd() to insert a node at the end of the linked list
* insertIndex() to insert a node at the given index of the linked list
* removeStart() to remove a node at the start of the linked list
* removeEnd() to remove a node at the end of the linked list
* removeIndex() to remove a node at the given index of the linked list
* removeData() to remove a node with the given data
* updateNode() to change the data of the node at the given index to the given data
* printList() to print the linked list


## Time Complexity of Operations
* insertStart(): O(1)
* insertEnd(): O(n)
* insertIndex(): O(1) best case, O(n) worst case, O(n) average case
* removeStart(): O(1)
* removeEnd(): O(n)
* removeIndex(): O(1) best case, O(n) worst case, O(n) average case
* removeData(): O(1) best case, O(n) worst case, O(n) average case
* updateNode(): O(1) best case, O(n) worst case, O(n) average case
* printList(): O(n)

## How Linked List Implementation Works:

### Input:

- A choice of operation from the above choices.

### Process: 

- The choice made by the user indicates which operation to perform. They are as follows:

1. insertStart():
    - Creates a new node to store the value given by the user.
    - Sets the newly created node to point towards the current head of the list.
    - Assigns the new node as the head of the list.

2. insertEnd():
    - Creates a new node to store the value given by the user.
    - Traverses to the end of the list.
    - Points the last node to the newly created node.

3. insertIndex():
    - Creates a new node to store the value given by the user.
    - Moves to the node before the index given by the user.
    - Points this node to the new node and points the new node to the node initially at that index.

4. removeStart():
    - Sets the 2nd node as the head of the list.

5. removeEnd():
    - Sets the 2nd last node to point toward an empty location.

6. removeIndex():
    - Moves to the node before the index given by the user.
    - Points this node to the node one ahead of the given index.

7. removeData():
    - Traverses to the node before the node that has the matching value.
    - Points this node to the one after the node with the given data.

8. updateNode():
    - Traverses to the node at the given index.
    - Changes the data to the given value.

9. printList():
    - Goes to each node and prints the value stored in that node.

### Output: 

- If the operation choice is any number between 0 and 10 (exclusive bounds), the program performs the corresponding operation and offers the choice to the user again. Otherwise, it indicates that the exit operation was triggered and ends the program.

## Key Features:

- Input Handling: 
    - The program prompts the user to input a choice of operation.
- Error Handling: 
    - The program checks for invalid inputs and handles exceptions like entering non-integer values.

## Example
### Input 1:
```bash
*********** Linked List Operations ***********
Choose from the following operations:
1. Insert node at start
2. Insert node at end
3. Insert node at given index
4. Remove node at start
5. Remove node at end
6. Remove node at given index
7. Remove node with given data
8. Update node at given index to given data
9. Print linked list
Enter any other value to exit

Choose an operation: 1
Enter the value to be inserted: 10
```

### Output 1:
```bash
10 Added to Start of Linked List
```

### Input 2:
```bash
Choose the next operation: 2
Enter the value to be inserted: 20
```

### Output 2:
```bash
20 Added to End of Linked List
```

### Input 3:
```bash
Choose the next operation: 3
Enter the value to be inserted: 30
Enter the index at which 30 is to be inserted: 1
```

### Output 3:
```bash
30 Added at index 1 of Linked List
```

### Input 4:
```bash
Choose the next operation: 3
Enter the value to be inserted: 40
Enter the index at which 40 is to be inserted: 2
```

### Output 4:
```bash
40 Added at index 2 of Linked List
```

### Input 5:
```bash
Choose the next operation: 3
Enter the value to be inserted: 50
Enter the index at which 50 is to be inserted: 0
```

### Output 5:
```bash
50 Added to Start of Linked List
```

### Input 6:
```bash
Choose the next operation: 4
```

### Output 6:
```bash
50 Removed from Start of Linked List
```

### Input 7:
```bash
Choose the next operation: 5
```

### Output 7:
```bash
20 Removed from End of Linked List
```

### Input 8:
```bash
Choose the next operation: 3
Enter the value to be inserted: 70
Enter the index at which 70 is to be inserted: 0
```

### Output 8:
```bash
70 Added to Start of Linked List
```

### Input 9:
```bash
Choose the next operation: 6
Enter the index to be removed: 1
```

### Output 9:
```bash
Index 1 removed from Linked List
```

### Input 10:
```bash
Choose the next operation: 7
Enter the value to be removed: 70
```

### Output 10:
```bash
70 found at index 0.
70 Removed from Start of Linked List
```

### Input 11:
```bash
Choose the next operation: 8
Enter the value to be updated: 90
Enter the index at which 90 is to be updated: 1
```

### Output 11:
```bash
Updated index 1 to 90
```

### Input 12:
```bash
Choose the next operation: 9
```

### Output 12:
```bash
The linked list: 30 -> 90
```

### Input 13 (Non-numeric input given):
```bash
Choose the next operation: p
```

### Output 13:
```bash
Exit Operation Triggered...
```

## Enhancements from Original Code
- This implementation improves upon the typical linked list implementation by:
    - Error Handling: The code includes exception handling to manage invalid user inputs like non-integer values, ensuring the program does not crash unexpectedly.
    - Menu Implementation: Lets the user add, remove and update elements in the list as they wish until they choose to exit the program.

## How to Run

- Clone the repository: 
    1. ``git clone github.com/<your-username>/<your-repository>.git ``
    2. ``cd PythonDS/LinkedList``

## Run the Python script:
- Run the following script
    1. ``python3 LinkedList.py``

### Contributing
Contributions are welcome! If you'd like to improve the implementation or suggest a new feature, follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them (git commit -m 'Add new feature').
4. Push to your branch (git push origin feature-branch).
5. Open a pull request.

### License
This project is licensed under the ``MIT License`` - see the LICENSE file for details.
