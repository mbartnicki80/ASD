def DFS2(G, v, visited2):
    n = len(G)
    visited2[v] = 1
    for i in range(n):
        if G[i][v] and visited2[i]==0:
            DFS2(G, i, visited2)
        

def Sklad(G):
    n = len(G)
    visited = [0 for i in range(n)]
    visited2 = [0 for i in range(n)]
    vert = []

    def DFS(G, v):
        visited[v] = 1
        for i in range(n):
            if G[v][i] and visited[i]==0:
                DFS(G, i)
        vert.append(v)

    for i in range(n):
        if visited[i]==0:
            DFS(G, i)

    sum = 0
    while len(vert)>0:
        a = vert.pop()
        if visited2[a]==0:
            DFS2(G, a, visited2)
            sum += 1
    return sum


def main():
    G = [
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]
        ]
    print(Sklad(G))
main()