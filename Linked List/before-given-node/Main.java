// Java Implementation to insert a node before
// a given key using iteratinon
class Node {
    int data;
    Node next;

    Node(int x) {
        data = x;
        next = null;
    }
}

public class Main {

    // Iterative function to insert a new node with value 
    // newData before the node with the key
    static Node insertBeforeKey(Node head, int key, 
                                int newData) {

        // Special case: if the key is at the head
        if (head == null) {
            return null;
        }
        if (head.data == key) {
            Node newNode = new Node(newData);
            newNode.next = head;
            return newNode;
        }

        // Initialize current and previous pointers
        Node curr = head;
        Node prev = null;

        // Traverse the list to find the key
        while (curr != null && curr.data != key) {
            prev = curr;
            curr = curr.next;
        }

        // If the key was found
        if (curr != null) {
            Node newNode = new Node(newData);
            prev.next = newNode;
            newNode.next = curr;
        }

        return head;
    }

    static void printList(Node node) {
        Node curr = node;
        while (curr != null) {
            System.out.print(curr.data + " ");
            curr = curr.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {

        // Create a hard-coded linked list:
        // 1 -> 2 -> 3 -> 4 -> 5
        Node head = new Node(1);
        head.next = new Node(2);
        head.next.next = new Node(3);
        head.next.next.next = new Node(4);
        head.next.next.next.next = new Node(5);

        int newData = 6;
        int key = 2;

        head = insertBeforeKey(head, key, newData);

        printList(head);
    }
}
