from kol2testy import runtests
from queue import PriorityQueue
'''
Mateusz Bartnicki
W celu rozwiazania tego problemu poszukuje najmniejszego drzewa rozpinajacego za pomoca algorytmu Prima. Gdy je znajde, sprawdzam, czy spelnia warunki zadania,
to znaczy, czy kazda krawedz spoza drzewa jest mniejsza od m lub wieksza od M. Jesli tak jest, zwracam sume drzewa, jesli nie, usuwam najmniejsza krawedz z grafu (zapamietujac
najmniejsza aktualnie krawedz i nie rozwazajac krawedzi mniejszych) i szukam nowego najmniejszego drzewa rozpinajacego. Procedurę powtarzam, aż drzewo nie będzie istniało lub 
znajdę takie, które spełnia warunki zadania.

Zlozonosc: O(E^2)
'''

def mst(G, v, minimum):

    n = len(G)
    ming = float('inf')
    Graph = [[0 for _ in range(n)] for _ in range(n)]
    Graph2 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j, d in G[i]:
            if d>minimum:
                Graph[i][j] = d
                Graph2[i][j] = d
                ming = min(ming, d)                     #tworze grafy pomocnicze
                                                        #Graph sluzy do pomocy w zliczaniu sumy krawedzi
                                                        #Graph2 pomaga pozniej w stwierdzeniu, czy drzewo spelnia warunki zadania

    distances = [float('inf') for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [0 for _ in range(n)]
    Q = PriorityQueue()
    distances[v] = 0
    Q.put((0, v))
    while not Q.empty():
        dist, vert = Q.get()
        visited[vert] = 1
        for v, d in G[vert]:
            if distances[v]>d and visited[v]==0 and d>minimum:
                distances[v] = d
                parent[v] = vert
                Q.put((distances[v], v))
                                                        #znajduje mst algoytmem prima
    mini = float('inf')
    maxi = 0
    sum = 0
    ile = 0
    for i in range(n):
        if parent[i]!=-1:
            sum += Graph[i][parent[i]]
            mini = min(Graph[i][parent[i]], mini)
            maxi = max(Graph[i][parent[i]], maxi)
            Graph2[i][parent[i]] = 0
            Graph2[parent[i]][i] = 0
        else:
            ile += 1
        if ile>=2:
            return None
                                                        #sumuje wartosci krawedzi drzewa, jednoczesnie znajduje minimum i maximum wartosci krawedzi drzewa
                                                        #oraz sprawdzam, czy każdy wierzchołek ma rodzica, czyli czy drzewo istnieje (0 nie ma rodzica, jest
                                                        # wierzchołkiem startowym)
    for i in range(n):
        for j in range(n):
            if Graph2[i][j]>mini and Graph2[i][j]<maxi:
                return mst(G, 0, ming)                  #sprawdzam czy drzewo spelnia zalozenia, jesli nie, tworze nowe bez rozwazania najmniejszej aktualnie krawedzi,
                                                        #jesli tak, zwracam sume

    return sum

def beautree(G):
    # tu prosze wpisac wlasna implementacje
    return mst(G, 0, 0)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
