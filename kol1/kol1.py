'''
Mateusz Bartnicki
Zadanie polega na szukaniu k-tego największego elementu w pewnych podziałach tablicy. W tym celu, dzielę tablicę w sposób określony w poleceniu, a następnie
algorytmem magicznych piątek szukam k-tego największego elementu w każdym zadanym przedziale i dodaję go do sumy, ktorą na końcu zwracam.
Szacowana złożoność czasowa: O(np)
Szacowana złożoność pamięciowa: O(np)
'''

from kol1testy import runtests

def bubble(T):
    n = len(T)
    for i in range(n):
        for j in range(1, n-i):
            if T[j]<T[j-1]:
                T[j], T[j-1] = T[j-1], T[j]
    return T

def mediana(T):
    bubble(T)
    return T[len(T)//2]

def partition(T, l, r):
    mediany = [mediana(T[i:min(i+5, r+1)]) for i in range(l, r+1, 5)]
    if len(mediany)<=5:
        piv = mediana(mediany)
    else:
        piv = qselect(mediany, len(mediany)//2, 0, len(mediany)-1)
    
    ind = 0
    for i in range(l, r+1):
        if T[i]==piv:
            ind = i
            break
    
    T[ind], T[r] = T[r], T[ind]
    i = l-1
    for j in range(l, r+1):
        if T[j]>=piv:
            i += 1
            T[i], T[j] = T[j], T[i]
    return i


def qselect(T, k, l, r):
    q = partition(T, l, r)
    if q==k:
        return T[q]
    elif q<k:
        return qselect(T, k, q+1, r)
    else:
        return qselect(T, k, l, q-1)
    

def ksum(T, k, p):
    n = len(T)
    sum = 0
    prev = -1
    for i in range(n-p+1):
        sum += qselect(T[i:i+p], k-1, 0, p-1)

    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
