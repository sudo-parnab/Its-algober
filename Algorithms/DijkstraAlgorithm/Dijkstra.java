import java.util.*;

class Graph {
    private Map<Integer, List<Pair>> adjList = new HashMap<>();

    private static class Pair {
        int vertex;
        int weight;
        Pair(int vertex, int weight) {
            this.vertex = vertex;
            this.weight = weight;
        }
    }

    public void addEdge(int u, int v, int weight) {
        adjList.putIfAbsent(u, new ArrayList<>());
        adjList.get(u).add(new Pair(v, weight));
        adjList.putIfAbsent(v, new ArrayList<>());
        adjList.get(v).add(new Pair(u, weight)); // For undirected graph
    }

    public Map<Integer, Integer> dijkstra(int start) {
        PriorityQueue<Pair> queue = new PriorityQueue<>(Comparator.comparingInt(a -> a.weight));
        Map<Integer, Integer> distances = new HashMap<>();
        for (int vertex : adjList.keySet()) {
            distances.put(vertex, Integer.MAX_VALUE);
        }
        distances.put(start, 0);
        queue.add(new Pair(start, 0));

        while (!queue.isEmpty()) {
            Pair current = queue.poll();
            for (Pair neighbor : adjList.getOrDefault(current.vertex, new ArrayList<>())) {
                int newDist = distances.get(current.vertex) + neighbor.weight;
                if (newDist < distances.get(neighbor.vertex)) {
                    distances.put(neighbor.vertex, newDist);
                    queue.add(new Pair(neighbor.vertex, newDist));
                }
            }
        }
        return distances;
    }

    // Example usage
    public static void main(String[] args) {
        Graph g = new Graph();
        g.addEdge(0, 1, 10);
        g.addEdge(0, 2, 5);
        g.addEdge(1, 2, 2);
        g.addEdge(1, 3, 1);
        g.addEdge(2, 1, 3);
        g.addEdge(2, 3, 9);
        g.addEdge(2, 4, 2);
        g.addEdge(3, 4, 6);
        g.addEdge(4, 3, 4);

        Map<Integer, Integer> distances = g.dijkstra(0);
        for (Map.Entry<Integer, Integer> entry : distances.entrySet()) {
            System.out.println("Distance from 0 to " + entry.getKey() + " is " + entry.getValue());
        }
    }
}
