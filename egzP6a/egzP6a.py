from egzP6atesty import runtests 
from random import randint

def merge(left, right, p):
    W = []
    i = 0; j = 0
    while i<len(left) and j<len(right):
        if left[i][p]>=right[j][p]:
            W.append(left[i])
            i += 1
        else:
            W.append(right[j])
            j += 1
    while i<len(left):
        W.append(left[i])
        i += 1
    while j<len(right):
        W.append(right[j])
        j += 1
    return W

def msort(T, p):
    n = len(T)
    if n<=1:
        return T
    mid = n//2
    left = msort(T[:mid], p)
    right = msort(T[mid:], p)
    return merge(left, right, p)

def google ( H, s ):
    T = []
    for i in range(len(H)):
        dl = 0
        for j in range(len(H[i])):
            if H[i][j]>='a' and H[i][j]<='z':
                dl += 1
        T.append((H[i], len(H[i]), dl))
    
    T = msort(T, 2)
    T = msort(T, 1)

    return T[s-1][0]


runtests ( google, all_tests=True )