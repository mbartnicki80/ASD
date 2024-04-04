from zad2testy import runtests
from queue import PriorityQueue
'''
Mateusz Bartnicki
Opis algorytmu:
Wystarczy tak naprawdę znaleźć maksymalne elementy, ponieważ nieważne jaką
drogę przejdziemy i w jakiej kolejności je weźmiemy, łączna suma śniegu
i czas potrzebny na zebranie go będzie takie same. W celu znalezienia wyniku
utworzę kopiec, który na samej górze (indeks 0) zawierać będzie element
maksymalny. Po każdym zabraniu maksymalnego elementu, będę naprawiać kopiec,
aby na górze znowu był maksymalny element. Procedurę będę powtarzać, aż
mój element - liczba dni nie będzie <= 0. Wtedy przerywam program i 
zwracam łączną sumę zebranego śniegu.
Szacowana złożoność: O(n logn)
'''
def parent(i):
    return (i-1)//2

def left(i):
    return i*2+1

def right(i):
    return i*2+2

def heapify(S, i, n):
    r = right(i)
    l = left(i)
    maxind = i
    if l<n and S[l]>S[maxind]:
        maxind = l
    if r<n and S[r]>S[maxind]:
        maxind = r
    if maxind != i:
        S[i], S[maxind] = S[maxind], S[i]
        heapify(S, maxind, n)

def buildheap(S):
    n = len(S)
    for i in range(parent(n-1), -1, -1):
        heapify(S, i, n)

def snow( S ):

    sum = 0; days = 0
    n = len(S)
    buildheap(S)
    sum = 0; days = 0
    while S:
        if S[0]-days<=0:
            break
        sum += S[0]-days
        days += 1
        S[0], S[n-days] = S[n-days], S[0]
        heapify(S, 0, n-days)
    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
