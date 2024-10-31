import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, weight):
        self.edges.setdefault(u, []).append((v, weight))
        self.edges.setdefault(v, []).append((u, weight))  # For undirected graph

    def dijkstra(self, start):
        queue = [(0, start)]
        distances = {node: float('infinity') for node in self.edges}
        distances[start] = 0

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            for neighbor, weight in self.edges.get(current_node, []):
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        return distances

# Example usage
g = Graph()
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 4)
g.add_edge(2, 3, 2)
distances = g.dijkstra(1)
print(distances)
