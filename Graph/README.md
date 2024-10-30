# Graph Algorithms

This project contains implementations of graph algorithms in Python, C, and Java. 

## Problem Overview

Graphs are fundamental data structures used to represent relationships between objects. A graph is composed of vertices (nodes) and edges (connections between nodes). One common operation on graphs is traversing them to explore their structure, which can be accomplished using algorithms like Depth First Search (DFS).

### Purpose

The purpose of this project is to provide a simple implementation of a graph data structure and demonstrate how to perform a Depth First Search (DFS) traversal on it.

### Implementations

- **Python**: The Python implementation uses a dictionary to represent the adjacency list of the graph. The `dfs` method performs a depth-first traversal, printing each visited vertex.
  
- **C**: The C implementation uses a 2D array to represent the graph's edges. The `dfs` function recursively traverses the graph and marks visited vertices using an array.

- **Java**: The Java implementation uses a HashMap to store the adjacency list of the graph. The `dfs` method utilizes a set to track visited vertices during traversal.

### Usage

To run the examples:

1. **Python**: Execute the `graph.py` file using Python 3.
2. **C**: Compile and run the `graph.c` file using a C compiler.
3. **Java**: Compile and run the `Graph.java` file using the Java Development Kit (JDK).

### Conclusion

This project serves as an introduction to graph data structures and demonstrates the implementation of depth-first search. Contributions are welcome to expand on this foundation with more complex algorithms and features.
