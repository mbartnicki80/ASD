from zad3testy import runtests
from random import randint
'''
Mateusz Bartnicki
Opis algorytmu:
Na początku obracam wszystkie napisy w ten sposób, aby zawsze napis[0]<=napis[len(napis)-1]. W ten sposób
mogę teraz posortować te napisy, a następnie liniowo znaleźć najdłuższy podciąg takich samych napisów.
Szacowana złożoność czasowa: O(NlogN)
'''
def quicksort(T, p, r):
    while p<r:
        q = partition(T, p, r)
        if q<(p+r)//2:
            quicksort(T, p, q-1)
            p = q+1
        else:
            quicksort(T, q+1, r)
            r = q-1

def partition(T, p, r):
    pivot = randint(p, r)
    T[pivot], T[r] = T[r], T[pivot]
    x = T[r]
    i = p-1
    for j in range(p, r):
        if T[j]<=x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1

def strong_string(T):
    n = len(T)
    for i in range(n):
        if T[i][0]>T[i][len(T[i])-1]:
            T[i] = T[i][::-1]
    quicksort(T, 0, n-1)
    maxsuma = 1
    suma = 1
    for i in range(1, n):
        if T[i]==T[i-1]:
            suma += 1
            maxsuma = max(maxsuma, suma)
        else:
            suma = 1
    return maxsuma


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
