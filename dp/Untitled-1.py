def knapsack(W, Z, l, n, DP):
    if n==0 or l==0:
        return 0
    if DP[n][l]!=-1:
        return DP[n][l]
    
    if W[n-1]<=l:
        DP[n][l] = max(Z[n-1]+knapsack(W, Z, l-W[n-1], n-1, DP), knapsack(W, Z, l, n-1, DP))
        return DP[n][l]
    elif W[n-1]>l:
        DP[n][l] = knapsack(W, Z, l, n-1, DP)
        return DP[n][l]
DP = [[-1 for i in range(l+1)] for i in range(n+1)]