def bellman(G, s):
    n = len(G)
    V = 0
    for i in range(n):
        V = max(V, G[i][0], G[i][1])
    distances = [float('inf') for _ in range(n+1)]
    parent = [-1 for _ in range(n+1)]
    distances[s] = 0
    
    for i in range(V-1):
        for j in range(n):
            if distances[G[j][1]]>distances[G[j][0]]+G[j][2]:
                distances[G[j][1]] = distances[G[j][0]]+G[j][2]
                parent[G[j][1]] = G[j][0]
    for i in range(n):
        if distances[G[i][1]] > distances[G[i][0]] + G[i][2]:
            return False, distances, parent
    return True, distances, parent

def main():
    G = [[0, 1, 3], [1, 2, 1], [2, 3, 2], [3, 4, 2], [3, 2, -7]]
    print(bellman(G, 0))
main()