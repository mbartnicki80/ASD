from egz2btesty import runtests

def magic( C ):
    n = len(C)
    T = [-1*float('inf') for i in range(n)]
    T[0] = 0
    for i in range(n-1):
        for j in range(1, len(C[i])):
            if (C[i][j][1]==-1 or T[i]==-1*float('inf')):
                continue
            if T[i]+C[i][0]>=C[i][j][0] and C[i][0]-C[i][j][0]<=10:
                T[C[i][j][1]] = max(T[C[i][j][1]], T[i]+min(10, C[i][0]-C[i][j][0]))
    if T[n-1] == -1*float('inf'):
        return -1
    return T[n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
