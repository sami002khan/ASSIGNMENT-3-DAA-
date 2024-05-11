
"""
  graph
   1 ---3--          
 /          \  
0            5---6
 \          /
  2 --- 4--
"""

class Edge:
    def __init__(self, source, dis):
        self.source = source
        self.dis = dis

def creategraph(graph):
    graph[0].append(Edge(0, 1))
    graph[0].append(Edge(0, 2))
    graph[1].append(Edge(1, 0))
    graph[1].append(Edge(1, 3))
    graph[2].append(Edge(2, 0))
    graph[2].append(Edge(2, 4))
    graph[3].append(Edge(3, 1))
    graph[3].append(Edge(3, 5))
    graph[4].append(Edge(4, 2))
    graph[4].append(Edge(4, 5))
    graph[5].append(Edge(5, 3))
    graph[5].append(Edge(5, 4))
    graph[5].append(Edge(5, 6))
    graph[6].append(Edge(6, 5))

def neighbours(graph):
    print("sourse\t dis\n")
    for i in range(7):
        e = graph[i][0]
        print(e.source, end='\t')
        for j in range(len(graph[i])):
            print(graph[i][j].dis, end=' ')
        print()
def BFS(graph):
    import queue
    q=queue.Queue()
    visted=[]
    q.put(0)
    visted.append(0)
    while not q.empty():
        curr=q.get()
        print(curr)
        
        for j in range(len(graph[curr])):
           dis= graph[curr][j].dis
           if dis not in visted:
               q.put(dis)
               visted.append(dis)
# Usage
V = 7
graph = [[] for _ in range(V)]
creategraph(graph)
print("neighbours\n")
neighbours(graph)
print('\nBFS\n')
BFS(graph)