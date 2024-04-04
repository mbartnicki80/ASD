from collections import deque

def BFS(G, s, t):
    n = len(G)
    visited = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [0 for _ in range(n)]
    Q = deque()
    Q.append(s)
    visited[s] = 1
    while Q:
        a = Q.popleft()
        if a==t:
            return visited, parent, d
        for v in G[a]:
            if visited[v]==0:
                Q.append(v)
                visited[v] = 1
                parent[v] = a
                d[v] = d[a] + 1
    return visited, parent, d