"""
Python implementation of Stack data structure using Linked List
The operations implemented are:
1. push() to insert an element into the stack.
2. pop() to remove an element from the stack.
3. isEmpty() returns true if stack is empty else false.
4. peek() Returns the top element of the stack.
"""

class Node:

    # Constructor to initialize a node for the linked list implementation
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    # Constructor to initialize the root
    def __init__(self):
        self.root = None

    # Function to check if the stack is empty
    def isEmpty(self):
        return True if self.root is None else False

    # Function to push element to the top of the stack
    def push(self, data):
        node = Node(data)
        node.next = self.root
        self.root = node
        print(f"{data} pushed to stack")

    # Function to pop the top-most element of the stack
    def pop(self):
        if (self.isEmpty()):
            print("No elements in the stack")
            return
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        print (f"{popped} popped from stack")

    # Function to display the top-most element of the stack without removing it from the stack
    def peek(self):
        if self.isEmpty():
            print("No elements in the stack")
            return
        peeked = self.root.data
        print (f"Top element is {peeked}")


# Driver code
stack = Stack()

print("*********** Stack Operations ***********")
print("Choose from the following operations:")
print("1. Push Element")
print("2. Pop Element")
print("3. Check If Stack Empty")
print("4. Peek Top Element")
print("Enter any other value to exit\n")

#Exception handling for user error in choice.
try:
    choice = int(input("Choose an operation: "))
    while choice > 0 and choice < 5:
        if choice == 1:
            data = int(input("Enter the value to be pushed: "))
            stack.push(data)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            if stack.isEmpty():
                print("There are no elements in the stack currently.")
            else:
                print("There are elements in the stack currently.")
        else:
            stack.peek()
        print()
        choice = int(input("Choose the next operation: "))
    print("Exit Operation Triggered...") #Prints when input is not between 0 and 4
except ValueError:
    print("Exit Operation Triggered...") #Prints when input is not numeric