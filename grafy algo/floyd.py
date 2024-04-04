def floyd(G):
    n = len(G)
    S = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                S[i][j] = 0
            elif G[i][j]!=-1:
                S[i][j] = G[i][j]

    for t in range(n):
        for x in range(n):
            for y in range(n):
                if S[x][y]>S[x][t]+S[t][y]:
                    S[x][y]=S[x][t]+S[t][y]
    return S

def main():
    G = [
        [-1, 3, -1, 3, -1, -1, -1, -1, 1],
        [3, -1, 5, -1, -1, -1, -1, -1, -1],
        [-1, 5, -1, 2, -1, 1, -1, -1, -1],
        [3, -1, 2, -1, 2, -1, 1, -1, -1],
        [-1, -1, -1, 2, -1, 8, -1, 1, -1],
        [-1, -1, 1, -1, 8, -1, -1, 4, -1],
        [-1, -1, -1, 1, -1, -1, 7, -1, 2],
        [-1, -1, -1, 1, -1, -1, -1, 7, 2],
        [1, -1, -1, -1, -1, -1, 2, -1, -1]
        ]
    print(floyd(G))
main()