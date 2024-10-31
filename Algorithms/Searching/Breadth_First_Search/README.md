# Graph Algorithms: Breadth First Search (BFS)

This project contains implementations of the Breadth First Search (BFS) algorithm in Python, C, and Java.

## Problem Overview

Graphs are fundamental data structures used to represent relationships between objects. A graph is composed of vertices (nodes) and edges (connections between nodes). One common operation on graphs is traversing them to explore their structure, which can be accomplished using algorithms like Breadth First Search (BFS).

### Purpose

The purpose of this project is to provide a simple implementation of a graph data structure and demonstrate how to perform a Breadth First Search (BFS) traversal on it.

### Implementations

- **Python**: The Python implementation uses a dictionary to represent the adjacency list of the graph. The `bfs` method performs a breadth-first traversal, printing each visited vertex.

- **C**: The C implementation uses a 2D array to represent the graph's edges. The `bfs` function utilizes a queue to traverse the graph iteratively and marks visited vertices using an array.

- **Java**: The Java implementation uses a HashMap to store the adjacency list of the graph. The `bfs` method utilizes a queue and a set to track visited vertices during traversal.

### Usage

To run the examples:

1. **Python**: Execute the `bfs.py` file using Python 3.
2. **C**: Compile and run the `bfs.c` file using a C compiler.
3. **Java**: Compile and run the `BFS.java` file using the Java Development Kit (JDK).

### Conclusion

This project serves as an introduction to graph data structures and demonstrates the implementation of breadth-first search. Contributions are welcome to expand on this foundation with more complex algorithms and features.
