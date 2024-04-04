from queue import PriorityQueue

def dijkstra(G, s):
    n = len(G)
    distances = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [0 for _ in range(n)]
    visited[s] = 1
    Q = PriorityQueue()
    distances[s] = 0
    Q.put((0, s))

    while not Q.empty():
        dist, v = Q.get()
        for u, d in G[v]:
            if visited[u]==0:
                if distances[u]>distances[v]+d:
                    distances[u] = distances[v]+d
                    parent[u] = v
                    Q.put((d+dist, u))
        visited[v] = 1
    return distances, parent
def main():
    G = [ (0, 1, 3), (1, 2, 5), (2, 5, 1), (2, 3, 2), (0, 3, 3),
         (3, 4, 2), (4, 5, 8), (4, 7, 1), (5, 7, 4), (6, 7, 7),
         (3, 6, 1), (6, 8, 2), (0, 8, 1) 
        ]
    n = 0
    for i in range(len(G)):
        n = max(n, G[i][0]+1, G[i][1]+1)

    Graph = [[] for _ in range(n)]
    for i in range(len(G)):
        Graph[G[i][0]].append((G[i][1], G[i][2]))
        Graph[G[i][1]].append((G[i][0], G[i][2]))
    print(dijkstra(Graph, 8))
main()