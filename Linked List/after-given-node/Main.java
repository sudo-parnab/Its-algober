// Java Program to Insert a Node after a Given Node in
// Linked List

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

public class Main {
  
    // Function to insert a new node after a given node
    static Node insertAfter(Node head, int key,
                                   int newData) {
        Node curr = head;

        // Iterate over Linked List to find the key
        while (curr != null) {
            if (curr.data == key)
                break;
            curr = curr.next;
        }

        // if curr becomes null means, given key is not
        // found in linked list
        if (curr == null)
            return head;

        // Allocate new node by given data and point
        // the next of newNode to curr's next &
        // point current next to newNode
        Node newNode = new Node(newData);
        newNode.next = curr.next;
        curr.next = newNode;
        return head;
    }

    static void printList(Node node) {
        while (node != null) {
            System.out.print(node.data + " ");
            node = node.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
      
        // Create the linked list 2->3->5->6
        Node head = new Node(2);
        head.next = new Node(3);
        head.next.next = new Node(5);
        head.next.next.next = new Node(6);

        int key = 3, newData = 4;
        head = insertAfter(head, key, newData);


        printList(head);
    }
}
