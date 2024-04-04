'''
Mateusz Bartnicki
W celu rozwiązania tego zadania zastosowałem algorytm Dijkstry poszukujący najkrótszej ścieżki.
Problem osobliwości rozwiązałem w ten sposób, że połączyłem je wszystkie w jeden wierzchołek, z którego można
trafić do każdej planety łączącej osobliwości. 
Szacowany czas: mlogn
'''

from zad5testy import runtests
from queue import PriorityQueue

def dijkstra(planety, n, a, b, czyosobl):

    distances = [float('inf') for _ in range(n)]
    distances[a] = 0
    visited = [0 for _ in range(n)]
    Q = PriorityQueue()
    Q.put((0, a))

    while not Q.empty():
        d, u = Q.get()
        if planety[u]!=None:
            for v, dist in planety[u]:
                if visited[v]==0:
                    if distances[v]>distances[u]+dist:
                        distances[v] = distances[u]+dist
                        Q.put((d+dist, v))
        else:  
            for v, dist in planety[n]:
                if visited[v]==0:
                    if distances[v]>distances[u]+dist:
                        distances[v] = distances[u]+dist
                        Q.put((d+dist, v))
        visited[u] = 1
        if czyosobl==1 and planety[u]==None:
            return distances[u]
        if u==b:
            break
    
    if visited[b]:
        return distances[b]
    else:
        return None

def spacetravel( n, E, S, a, b ):
    
    planety = [[] for _ in range(n)]
    for i in range(len(E)):
        planety[E[i][0]].append((E[i][1], E[i][2]))
        planety[E[i][1]].append((E[i][0], E[i][2]))
    lista = []
    czyosobl = 0
    for i in S:
        for j in range(len(planety[i])):
            lista.append(planety[i][j])
        planety[i] = None
        if i==b:
            czyosobl = 1
    planety.append(lista)
    return dijkstra(planety, n, a, b, czyosobl)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )