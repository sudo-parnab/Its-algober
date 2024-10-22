"""
Python implementation of Linked List data structure
The operations implemented are:

1. insertStart() to insert a node at the start of the linked list
2. insertEnd() to insert a node at the end of the linked list
3. insertIndex() to insert a node at the given index of the linked list
4. removeStart() to remove a node at the start of the linked list
5. removeEnd() to remove a node at the end of the linked list
6. removeIndex() to remove a node at the given index of the linked list
7. removeData() to remove a node with the given data
8. updateNode() to change the data of the node at the given index to the given data
9. printList() to print the linked list
"""

class Node:

    # Constructor to initialize a node for the linked list implementation
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    # Constructor to initialize the root of the linked list
    def __init__(self):
        self.root = None
    
    # Function to insert node at the head of the list
    def insertStart(self, data):
        node = Node(data)
        node.next = self.root
        self.root = node
        print(f"{data} Added to Start of Linked List")
    
    # Function to insert node at the end of the list
    def insertEnd(self, data):
        node = Node(data)
        last = self.root
        if last == None:
            self.root = node
        else:
            while last.next != None:
                last = last.next
            last.next = node
        print(f"{data} Added to End of Linked List")

    # Function to insert node at the given index of the list
    def insertIndex(self, data, index):
        node = Node(data)
        start = self.root
        if index == 0:
            self.insertStart(data)
            return

        count = 0
        while count < index - 1 and start.next != None:
            start = start.next
            count += 1
        
        if start.next == None:
            print("Index higher than linked list, adding element to end of list")
            self.insertEnd(data)
            return
        
        node.next = start.next
        start.next = node
        print(f"{data} Added at index {index} of Linked List")
    
    # Function to remove node at the head of the list
    def removeStart(self):
        if self.root == None:
            print("No elements to remove")
            return
        value = self.root.data
        self.root = self.root.next
        print(f"{value} Removed from Start of Linked List")

    # Function to remove node at the end of the list
    def removeEnd(self):
        if self.root == None:
            print("No elements to remove")
            return
        node = self.root
        if node.next == None:
            print("Only one element in list, Removing from start...")
            self.removeStart()
            return

        while node.next.next != None:
            node = node.next
        value = node.next.data
        node.next = None
        print(f"{value} Removed from End of Linked List")

    # Function to remove node at the given index of the list
    def removeIndex(self, index):
        start = self.root
        if index == 0:
            self.removeStart()
            return

        count = 0
        while count < index - 1 and start.next != None:
            start = start.next
            count += 1
        
        if start.next == None:
            print("Index higher than linked list, cannot remove")
            return
        
        start.next = start.next.next
        print(f"Index {index} removed from Linked List")
    
    #Function to remove a node with the given data
    def removeData(self, val):
        start = self.root
        if start == None:
            print(f"{val} not found")
            return
        if start.data == val:
            print(f"{val} found at index 0.")
            self.removeStart()
            return
        count = 1
        while start.next != None:
            if start.next.data == val:
                print(f"{val} found at index {count}.")
                self.removeIndex(count)
                return
            count += 1
            start = start.next
        print(f"{val} not found.")

    # Function to change the data of the node at the given index to the given data
    def updateNode(self, val, index):
        start = self.root
        index_copy = index
        if start == None:
            print("No elements to update")
            return
        while index != 0 and start.next != None:
            start = start.next
            index -= 1
        if index == 0:
            start.data = val
            print(f"Updated index {index_copy} to {val}")
        else:
            print(f"Index greater than length of list.")
        
    # Function to print the linked list
    def printList(self):
        start = self.root
        if start == None:
            print("No elements added to the list")
            return
        print("The linked list: ", end = "")
        while start.next != None:
            print(f"{start.data} -> ", end = "")
            start = start.next
        print(start.data)

list = LinkedList()

print("*********** Linked List Operations ***********")
print("Choose from the following operations:")
print("1. Insert node at start")
print("2. Insert node at end")
print("3. Insert node at given index")
print("4. Remove node at start")
print("5. Remove node at end")
print("6. Remove node at given index")
print("7. Remove node with given data")
print("8. Update node at given index to given data")
print("9. Print linked list")
print("Enter any other value to exit\n")

#Exception handling for user error in choice.
try:
    choice = int(input("Choose an operation: "))
    while choice > 0 and choice < 10:
        if choice == 1:
            data = int(input("Enter the value to be inserted: "))
            list.insertStart(data)
        elif choice == 2:
            data = int(input("Enter the value to be inserted: "))
            list.insertEnd(data)
        elif choice == 3:
            data = int(input("Enter the value to be inserted: "))
            index = int(input(f"Enter the index at which {data} is to be inserted: "))
            list.insertIndex(data, index)
        elif choice == 4:
            list.removeStart()
        elif choice == 5:
            list.removeEnd()
        elif choice == 6:
            index = int(input(f"Enter the index to be removed: "))
            list.removeIndex(index)
        elif choice == 7:
            data = int(input(f"Enter the value to be removed: "))
            list.removeData(data)
        elif choice == 8:
            data = int(input("Enter the value to be updated: "))
            index = int(input(f"Enter the index at which {data} is to be updated: "))
            list.updateNode(data, index)
        else:
            list.printList()
        print()
        choice = int(input("Choose the next operation: "))
    print("Exit Operation Triggered...") #Prints when input is not between 0 and 10
except ValueError:
    print("Exit Operation Triggered...") #Prints when input is not numeric