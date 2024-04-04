from zad8ktesty import runtests 

def naprawdp(s, t, n, m, DP):
    if n==0:
        return m
    if m==0:
        return n
    
    if DP[n][m]!=-1:
        return DP[n][m]
    
    if s[n-1] == t[m-1]:
        DP[n][m] = naprawdp(s, t, n-1, m-1, DP)
        return DP[n][m]
    else:
        DP[n][m] = 1 + min(naprawdp(s, t, n-1, m, DP), naprawdp(s, t, n, m-1, DP), naprawdp(s, t, n-1, m-1, DP))
        return DP[n][m]

def napraw ( s, t ):
    DP = [[-1 for i in range(len(t)+1)] for j in range(len(s)+1)]
    return naprawdp(s, t, len(s), len(t), DP)

runtests ( napraw )