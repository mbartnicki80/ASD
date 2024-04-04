def most(G):
    n = len(G)
    visited = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    low = [0 for _ in range(n)]
    d = [0 for _ in range(n)]
    mosty = []
    time = 1

    def DFS(G, v):
        nonlocal time
        visited[v] = 1
        d[v] = low[v] = time
        time += 1
        for i in range(n):
            if parent[v]!=i and G[v][i]:
                if visited[i]==0:
                    parent[i] = v
                    DFS(G, i)
                    low[v] = min(low[v], low[i])
                else:
                    low[v] = min(low[v], d[i])

    DFS(G, 0)
    
    for i in range(n):
        if d[i]==low[i] and parent[i]>=0:
            mosty.append((i, parent[i]))

    return mosty

def main():
    G = [
        [0, 1, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0]
        ]
    print(most(G))
main()