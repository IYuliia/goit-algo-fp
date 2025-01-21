import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices  
        self.graph = {i: [] for i in range(vertices)}  

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  

def dijkstra(graph, start):
    dist = {i: float('inf') for i in range(graph.V)}  
    prev = {i: None for i in range(graph.V)} 
    dist[start] = 0

    min_heap = [(0, start)]  
    
    while min_heap:
        current_dist, u = heapq.heappop(min_heap)
       
        if current_dist > dist[u]:
            continue
      
        for v, weight in graph.graph[u]:
            alt = dist[u] + weight
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(min_heap, (alt, v))  

    return dist, prev

def get_shortest_path(prev, target):
    path = []
    while target is not None:
        path.append(target)
        target = prev[target]
    return path[::-1] 

graph = Graph(6)
graph.add_edge(0, 1, 7)
graph.add_edge(0, 2, 9)
graph.add_edge(0, 5, 14)
graph.add_edge(1, 2, 10)
graph.add_edge(1, 3, 15)
graph.add_edge(2, 3, 11)
graph.add_edge(2, 5, 2)
graph.add_edge(3, 4, 6)
graph.add_edge(4, 5, 9)

start_vertex = 0
distances, previous = dijkstra(graph, start_vertex)

for vertex in range(graph.V):
    print(f"Відстань від {start_vertex} до {vertex}: {distances[vertex]}")
    path = get_shortest_path(previous, vertex)
    print(f"Шлях: {path}")
