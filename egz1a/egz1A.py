from egz1Atesty import runtests
from queue import PriorityQueue

'''
Mateusz Bartnicki
W celu rozwiązania tego problemu, posłużę się algorytmem Dijkstry.
A mianowicie, najpierw tworzę graf G2, który będzie zawierać drogi już po napadzie (czyli te droższe)
Później w pętli for sprawdzę, który bank będzie najkorzystniej obrabować, czyli znajdę drogę z s do banku i algorytmem Dijkstry, odejmę sumę
uzyskaną z napadu, a następnie znajdę drogę w grafie G2 z banku do wierzchołka końcowego t.
Odpowiedzią jest minimum z uzyskanych wyników.
Szacowana złożoność: O(V*VlogV)
'''

def dijkstra(G, s, t):
    n = len(G)
    distances = [float('inf') for _ in range(n)]
    visited = [0 for _ in range(n)]
    visited[s] = 1
    Q = PriorityQueue()
    distances[s] = 0
    Q.put((0, s))

    while not Q.empty():
        dist, v = Q.get()
        for u, d in G[v]:
            if visited[u]==0:
                if distances[u]>distances[v]+d:
                    distances[u] = distances[v]+d
                    Q.put((d+dist, u))
        visited[v] = 1
    return distances[t]

def gold(G,V,s,t,r):
  n = len(G)
  G2 = [[] for _ in range(n)] #graf o zwiększonych kosztach
  
  for i in range(n):
    for v, d in G[i]:
      G2[i].append((v, d*2+r))
  mini = float('inf')

  for i in range(n):
    if i!=s:
      koszt = dijkstra(G, s, i)
      if i!=t:
        mini = min(mini, koszt-V[i]+dijkstra(G2, i, t))
      else:
        mini = min(mini, koszt-V[i])
    else:
       mini = min(mini, dijkstra(G, s, t))
  return mini

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
