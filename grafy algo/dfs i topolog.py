def DFS(G):
    n = len(G)
    visited = [0 for _ in range(n)]
    parent = [None for _ in range(n)]
    lista = []

    def DFSVisit(G, v):
        visited[v] = 1
        for u in G[v]:
            if visited[u]==0:
                parent[u] = v
                DFSVisit(G, u)
        lista.append(v)
                

    for i in range(n):
        if visited[i]==0:
            DFSVisit(G, i)
        
    return lista

def main():
    G = [
    [1, 2],
    [2, 3],
    [4],
    [],
    [],
    ]
    time = DFS(G)
    print(time)
main()