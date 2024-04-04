from kol1btesty import runtests
from random import randint

def partition(T, l, r):
    q = randint(l, r)
    T[q], T[r] = T[r], T[q]
    x = T[r]
    i = l-1
    for j in range(l, r+1):
        if T[j]<=x:
            i += 1
            T[i], T[j] = T[j], T[i]
    return i

#def radix(T, maxlen):

    #for i in range(maxlen-1, -1, -1):
    

def qs(T, l, r):
    while l<r:
        q = partition(T, l, r)
        if q-l<r-q:
            qs(T, l, q-1)
            l = q+1
        else:
            qs(T, q+1, r)
            r = q-1
    return T

def f(T):
    
    #maxlen = 0
    newT = [[] for _ in range(len(T))]
    for i in range(len(T)):
        for j in range(len(T[i])):
            newT[i].append(ord(T[i][j]))
        #qs(newT[i], 0, len(newT[i])-1)
        newT[i] = sorted(newT[i])
        #maxlen = max(maxlen, len(newT[i]))
    
    #qs(newT, 0, len(newT)-1)
    newT = sorted(newT)
    suma = 1; maxsuma = 1
    for i in range(1, len(newT)):
        if len(newT[i-1])==len(newT[i]):
            for j in range(len(newT[i])):
                if newT[i-1][j]!=newT[i][j]:
                    suma = 1
                    break
            else:
                suma += 1
                maxsuma = max(maxsuma, suma)
        else:
            suma = 1

    return maxsuma


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
