from queue import PriorityQueue

def prim(G, v):
    n = len(G)
    distances = [float('inf') for _ in range(n)]
    visited = [0 for _ in range(n)]
    visited[v] = 1
    distances[v] = 0
    parent = [-1 for _ in range(n)]
    Q = PriorityQueue()
    Q.put((0, v))

    while not Q.empty():
        dist, vert = Q.get()
        visited[vert] = 1
        for i in range(n):
            if G[vert][i] and visited[i]==0:
                if distances[i]>G[vert][i]:
                    parent[i] = vert
                    distances[i] = G[vert][i]
                    Q.put((distances[i], i))

    res = []
    for i in range(n):
        if parent[i]!=-1:
            res.append((i, parent[i], distances[i]))
    return res

def main():
    G = [ []
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
    print(prim(G, 8))
main()