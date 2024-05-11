
"""
  graph
   1 ---3--          
 /          \  
0            5---6
 \          /
  2 --- 4--
  
  Time Complexity of Dijkstra's Algorithm 
  O ( V 2 )
Time Complexity of Dijkstra's Algorithm is O ( V 2 )
 but with min-priority queue it drops down to O ( V + E l o g V ) 
"""
import heapq
import sys
class Edge:
    def __init__(self, destination, weight):
        self.destination = destination
        self.weight = weight
def dijkstra(graph, source):
    V = len(graph)
    distances = [float('inf')] * V
    distances[source] = 0
    pq = []
    heapq.heappush(pq, (0, source)) 
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_distance > distances[current_node]:
            continue
        for edge in graph[current_node]:
            neighbor = edge.destination
            weight = edge.weight
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
V = 7
graph = [[] for _ in range(V)]
def create_graph(graph):
    graph[0].append(Edge(1, 1))
    graph[0].append(Edge(2, 2))
    graph[1].append(Edge(0, 1))
    graph[1].append(Edge(3, 3))
    graph[2].append(Edge(0, 2))
    graph[2].append(Edge(4, 4))
    graph[3].append(Edge(1, 3))
    graph[3].append(Edge(5, 5))
    graph[4].append(Edge(2, 4))
    graph[4].append(Edge(5, 1))
    graph[5].append(Edge(3, 5))
    graph[5].append(Edge(4, 1))
    graph[5].append(Edge(6, 2))
    graph[6].append(Edge(5, 2))
create_graph(graph)
source_node = 0
shortest_distances = dijkstra(graph, source_node)
print("Shortest distances from node", source_node, "to all other nodes:")
for node in range(V):
    print("Node", node, "- Distance:", shortest_distances[node])
