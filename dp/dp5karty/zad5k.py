from zad5ktesty import runtests

def dp(A, i, j, DP):
    if i==j:
        return A[i]
    
    if DP[i][j]!=-1:
        return DP[i][j]
    
    DP[i][j] = max(A[i]-dp(A, i+1, j, DP), A[j]-dp(A, i, j-1, DP))
    return DP[i][j]

def garek ( A ):
    DP = [[-1 for i in range(len(A))] for j in range(len(A))]
    dp(A, 0, len(A)-1, DP)
    suma = 0
    for i in range(len(A)):
        suma += A[i]
    return ((suma-DP[0][len(A)-1])/2+DP[0][len(A)-1])

runtests ( garek )