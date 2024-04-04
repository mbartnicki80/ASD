class Node:
    def __init__(self, value):
        self.parent = self
        self.rank = 0
        self.value = value

def findset(x):
    if x.parent!=x:
        x.parent = findset(x.parent)
    return x.parent
    
def union(x, y):
    x = findset(x)
    y = findset(y)
        
    if x.rank>y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank==y.rank:
            y.rank += 1

def ranga(x, y):
    return findset(x)==findset(y)

def kruskal(G):
    n = len(G)
    G.sort(key=lambda x:x[2])
    Nodes = [Node(i) for i in range(n)]
    V = [[] for _ in range(n)]
    for v, u, d in G:
        if not ranga(Nodes[v], Nodes[u]):
            union(Nodes[v], Nodes[u])
            V[v].append(u)
            V[u].append(v)
    return V


def main():
    G = [ (0, 1, 3), (0, 3, 3), (0, 8, 1), (6, 8, 2),
         (1, 2, 5), (2, 3, 2), (3, 6, 1), (3, 8, 2),
         (2, 5, 1), (5, 7, 4), (4, 7, 1), (6, 7, 7)]
    print(kruskal(G))
main()