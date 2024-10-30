// Java Program to Insert a Node at the End of Linked List

class Node {
    int data;
    Node next;

    Node(int newData) {
        data = newData;
        next = null;
    }
}

public class Main {

    // Function appends a new node at the end and returns
    // the head.
    static Node insertAtEnd(Node head, int newData)
    {

        // Create a new node
        Node newNode = new Node(newData);

        // If the Linked List is empty, make the new
        // node as the head and return
        if (head == null) {
            return newNode;
        }

        // Store the head reference in a temporary variable
        Node last = head;

        // Traverse till the last node
        while (last.next != null) {
            last = last.next;
        }

        // Change the next pointer of the
        // last node to point to the new node
        last.next = newNode;

        // Return the head of the list
        return head;
    }

    public static void printList(Node node)
    {
        while (node != null) {
            System.out.print(" " + node.data);
            node = node.next;
        }
    }

    public static void main(String[] args)
    {
        // Create a linked list:
        // 2 -> 3 -> 4 -> 5 -> 6
        Node head = new Node(2);
        head.next = new Node(3);
        head.next.next = new Node(4);
        head.next.next.next = new Node(5);
        head.next.next.next.next = new Node(6);

        head = insertAtEnd(head, 1);
        printList(head);
    }
}
