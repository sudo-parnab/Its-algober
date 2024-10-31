#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define MAX 100

typedef struct {
    int edges[MAX][MAX];
    int numVertices;
} Graph;

void initGraph(Graph *g, int vertices) {
    g->numVertices = vertices;
    for (int i = 0; i < MAX; i++)
        for (int j = 0; j < MAX; j++)
            g->edges[i][j] = (i == j) ? 0 : INT_MAX;
}

void addEdge(Graph *g, int u, int v, int weight) {
    g->edges[u][v] = weight;
    g->edges[v][u] = weight;  // For undirected graph
}

void dijkstra(Graph *g, int start) {
    int distances[MAX];
    int visited[MAX] = {0};

    for (int i = 0; i < g->numVertices; i++) {
        distances[i] = INT_MAX;
    }
    distances[start] = 0;

    for (int count = 0; count < g->numVertices - 1; count++) {
        int minDist = INT_MAX, minIndex;
        for (int v = 0; v < g->numVertices; v++) {
            if (!visited[v] && distances[v] <= minDist) {
                minDist = distances[v];
                minIndex = v;
            }
        }
        visited[minIndex] = 1;

        for (int v = 0; v < g->numVertices; v++) {
            if (!visited[v] && g->edges[minIndex][v] != INT_MAX &&
                distances[minIndex] + g->edges[minIndex][v] < distances[v]) {
                distances[v] = distances[minIndex] + g->edges[minIndex][v];
            }
        }
    }

    // Print distances
    for (int i = 0; i < g->numVertices; i++) {
        printf("Distance from %d to %d is %d\n", start, i, distances[i]);
    }
}

// Example usage
int main() {
    Graph g;
    initGraph(&g, 5);
    addEdge(&g, 0, 1, 10);
    addEdge(&g, 0, 2, 5);
    addEdge(&g, 1, 2, 2);
    addEdge(&g, 1, 3, 1);
    addEdge(&g, 2, 1, 3);
    addEdge(&g, 2, 3, 9);
    addEdge(&g, 2, 4, 2);
    addEdge(&g, 3, 4, 6);
    addEdge(&g, 4, 3, 4);

    dijkstra(&g, 0);
    return 0;
}
