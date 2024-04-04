'''
Mateusz Bartnicki
W celu rozwiązania tego problemu, najpierw szukam najkrótszej ścieżki z wierzchołka s do wierzchołka t za pomocą algorytmu BFS.
Po znalezieniu najkrótszej ścieżki, sprawdzam, czy jest możliwe wydłużenie ścieżki, usuwając (w najgorszym przypadku) każdą możliwą krawędź 
z tej ścieżki. Jeśli w którymś momencie droga się wydłuży, zwracam krawędź, którą usunąłem. Jeśli żadna krawędź nie wydłuża drogi, zwracam None
Szacowana złożoność: O((V+E)*E)
'''

from zad4testy import runtests
import collections


def BFS(G, s, t, n):
    Q = collections.deque()
    visited = [0 for _ in range(n)]
    d = [-1 for _ in range(n)]
    parent = [None for i in range(n)]
    Q.append(s)
    visited[s] = 1
    d[s] = 0

    while Q:
        u = Q.popleft()
        if u==t:
            return d, parent
        for i in range(len(G[u])):
            if G[u][i]!=None and visited[G[u][i]]==0:
                visited[G[u][i]] = 1
                parent[G[u][i]] = u
                d[G[u][i]] = d[u]+1
                Q.append(G[u][i])
    return None

def nowadroga(G, s, t, n, q, r, odl):
    ind1 = 0; ind2 = 0; v1 = 0; v2 = 0
    for i in range(len(G[r])):
        if G[r][i]==q:
            ind1 = i
            v1 = G[r][i]
            G[r][i] = None #usuwam ostatnia krawedz wychodzaca z t w sciezce
            break

    for i in range(len(G[q])):
        if G[q][i]==r:
            ind2 = i
            v2 = G[q][i]
            G[q][i] = None
            break

    if BFS(G, s, t, n)!=None:
        d1, parent1 = BFS(G, s, t, n) #sprawdzam ponownie sciezke
    else:
        return (q, r)
    
    if d1[t]!=odl:
        return (q, r)
    else:
        G[r][ind1] = v1
        G[q][ind2] = v2
        return None

def longer( G, s, t ):
    # tu prosze wpisac wlasna implementacje
    n = 0
    for i in range(len(G)):
        for j in range(len(G[i])):
            n = max(n, G[i][j]+1)

    if BFS(G, s, t, n)!=None:
        d, parent = BFS(G, s, t, n) #szukam sciezki i dlugosci, czy istnieje
    else:
        return None
    
    q, r = parent[t], t
    odl = d[t]

    for i in range(d[t]):
        if q!=None:
            if nowadroga(G, s, t, n, q, r, odl)!=None:
                return nowadroga(G, s, t, n, q, r, odl)
        q, r = parent[q], q
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )