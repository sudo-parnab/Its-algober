# Graph Algorithms: Dijkstra's Algorithm

This project contains implementations of Dijkstra's Algorithm in Python, C, and Java.

## Problem Overview

Graphs are fundamental data structures used to represent relationships between objects. A graph is composed of vertices (nodes) and edges (connections between nodes). Dijkstra's Algorithm is a popular method for finding the shortest path from a starting vertex to all other vertices in a weighted graph.

### Purpose

The purpose of this project is to provide a simple implementation of a graph data structure and demonstrate how to perform Dijkstra's Algorithm for finding the shortest paths.

### Implementations

- **Python**: The Python implementation uses a dictionary to represent the adjacency list of the graph. The `dijkstra` method computes the shortest paths from the starting vertex, returning a dictionary of distances.

- **C**: The C implementation uses a 2D array to represent the graph's edges. The `dijkstra` function calculates the shortest paths using a standard iterative approach.

- **Java**: The Java implementation uses a HashMap to store the adjacency list of the graph. The `dijkstra` method computes the shortest paths from the starting vertex, returning a map of distances.

### Usage

To run the examples:

1. **Python**: Execute the `dijkstra.py` file using Python 3.
2. **C**: Compile and run the `dijkstra.c` file using a C compiler.
3. **Java**: Compile and run the `Dijkstra.java` file using the Java Development Kit (JDK).

### Conclusion

This project serves as an introduction to graph data structures and demonstrates the implementation of Dijkstra's Algorithm. Contributions are welcome to expand on this foundation with more complex algorithms and features.
