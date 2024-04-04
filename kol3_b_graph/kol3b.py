from kol3btesty import runtests

def dijkstra(G, s, t):
    n = len(G)
    distances = [float('inf') for _ in range(n)]
    visited = [0 for _ in range(n)]
    distances[s] = 0
    v = s
    found = 1
    while found:
        found = 0
        visited[v] = 1
        for i in range(n):
            if G[v][i] and visited[i]==0:
                if distances[i]>distances[v]+G[v][i]:
                    distances[i] = distances[v]+G[v][i]
        mini = float('inf')
        for i in range(n):
            if distances[i]<mini and visited[i]==0:
                mini, v, found = distances[i], i, 1

    return distances[t]

def airports( G, A, s, t ):
    n = len(G)
    Graph = [[float('inf') for i in range(n)] for j in range(n)]
    for i in range(n):
        for v, d in G[i]:
            Graph[i][v] = d
    for i in range(n):
        for j in range(n):
            if i!=j:
                Graph[i][j] = min(A[i]+A[j], Graph[i][j])
    for i in range(n):
        Graph[i][i] = 0
    return dijkstra(Graph, s, t)
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )