from queue import PriorityQueue


def dijkstra(G, s, t):
    n = len(G)
    distances = [float('inf') for _ in range(n)]
    distances[s] = 0
    parent = [-1 for _ in range(n)]
    visited = [0 for _ in range(n)]
    Q = PriorityQueue()
    Q.put((0, s))

    while not Q.empty():
        dist, a = Q.get()
        visited[a] = 0
        for i in range(n):
            if G[a][i] and visited[i]==0:
                if distances[i]>distances[a]+G[a][i]:
                    distances[i] = distances[a]+G[a][i]
                    parent[i] = a
                    Q.put((dist+G[a][i], i))
        
    return distances, parent

def main():
    G = [
        [0, 3, 0, 3, 0, 0, 0, 0, 1],
        [3, 0, 5, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 2, 0, 1, 0, 0, 0],
        [3, 0, 2, 0, 2, 0, 1, 0, 0],
        [0, 0, 0, 2, 0, 8, 0, 1, 0],
        [0, 0, 1, 0, 8, 0, 0, 4, 0],
        [0, 0, 0, 1, 0, 0, 7, 0, 2],
        [0, 0, 0, 1, 0, 0, 0, 7, 2],
        [1, 0, 0, 0, 0, 0, 2, 0, 0]
        ]
    print(dijkstra(G, 8, 4))
main()