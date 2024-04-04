def parent(i):
    return (i-1)//2

def right(i):
    return i*2+2

def left(i):
    return i*2+1

def heapify(tab, i, n):
    l = left(i)
    r = right(i)
    maxind = i
    if l<n and tab[l]<tab[maxind]:
        maxind = l
    if r<n and tab[r]<tab[maxind]:
        maxind = r
    if maxind!=i:
        tab[i], tab[maxind] = tab[maxind], tab[i]
        heapify(tab, maxind, n)
    
def buildheap(tab):
    n = len(tab)
    for i in range(parent(n-1), -1, -1):
        heapify(tab, i, n)

def ksort(tab, k):
    tabpom = []
    wynik = []
    for i in range(k+1):
        tabpom.append(tab[i])
    buildheap(tabpom)
    for i in range(k+1, len(tab)):
        q = tabpom[0]
        wynik.append(q)
        tabpom[0] = tab[i]
        heapify(tabpom, 0, len(tabpom))

    while len(tabpom)>0:
        wynik.append(tabpom.pop(0))
        heapify(tabpom, 0, len(tabpom))
    return wynik


if __name__=="__main__":
    tab = [2, 1, 0, 4, 3, 6, 5, 8, 9]
    print(ksort(tab, 2))