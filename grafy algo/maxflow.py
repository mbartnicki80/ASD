from queue import Queue
from math import inf

def max_flow(E, start, dest):
    flowsum = 0
    while True:
        parent = [-1 for _ in range(len(E))]
        parent[start] = None
        q = Queue()
        q.put((start, inf))
        flow = -1
        while not q.empty():
            vert, mini = q.get()
            for i in range(len(E)):
                if parent[i]==-1 and E[vert][i]:
                    parent[i] = vert
                    if i==dest: 
                        flow = min(mini, E[vert][i])
                        break
                    q.put((i, min(mini, E[vert][i])))
                    
        if flow<=0:
            return flowsum
        flowsum += flow
        z = dest
        while z!=start: 
            E[parent[z]][z] -= flow
            E[z][parent[z]] += flow
            z = parent[z]
        
    
if __name__=="__main__":
    n, m = map(int, input().split())
    E = [[0 for _ in range(n+1)] for _ in range(n+1)]
    tup = [() for i in range(m)]
    for i in range(m): 
        a, b, c = tuple(map(int, input().split()))
        E[a][b]=c
        
    print(max_flow(E, 1, n))