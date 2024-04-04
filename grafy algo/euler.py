def Euler(G, s, start):
    cycle = []
    n = len(G)
    def DFS(G, v):
        for i in range(start[v], n):
            if G[v][i]:
                G[v][i] = 0
                G[i][v] = 0
                start[v] = i
                DFS(G, i)
        cycle.append(v)

    DFS(G, s)
    return cycle, sum

def main():
    G = [
        [0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 0]
        ]
    start = [0 for i in range(len(G))]
    print(Euler(G, 0, start))
main()