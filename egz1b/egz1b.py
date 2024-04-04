from egz1btesty import runtests
'''
Mateusz Bartnicki
Aby rozwiązać ten problem, używam programowania dynamicznego.
W tym celu rozważam funkcję f(i, j) z polecenia.
Aby ją wykorzystać, tworzę tablicę DP, w której będę spamiętywać najmniejszy aktualnie koszt dostania się na planetę i posiadając j litrów paliwa,
czyli DP[i][j] = koszt dostania się na planetę i posiadając j litrów paliwa.
DP[0][i], jako "przypadek graniczny" wypełniam w ten sposób, że tankuje paliwo na pierwszej planecie do i litrów, czyli wynik w niej będzie C[0]*i
Następnie rozważam od razu teleport, czyli moja tablica DP[(numer planety, do której mogę się teleportować)][0] (0, bo tyle musi byc paliwa, aby użyc teleportu), będzie od razu
ceną teleportu.
Resztę tablicy DP będę uzupełniać w taki sposób, że będę rozważać 3 przypadki: aktualną cenę w niej (mogłem się teleportować), cenę, gdybym tam doleciał używając tylko paliwa z 
poprzedniej planety, lub cenę, gdybym tam doleciał z poprzedniej planety i dotankował resztę na aktualnej. Do tablicy DP wpiszę minimum z tych 3 przypadków.
Moim wynikiem jest minimum z DP[n-1][0] (bo najtaniej będzie tam dolecieć nie zostawiając nadmiarowego paliwa)
Szacowana złożoność: O(nE)
'''

def planets( D, C, T, E ):
    n = len(D)
    DP = [[float('inf') for _ in range(E+1)] for _ in range(n)]
    for i in range(E+1):
        DP[0][i] = i*C[0]
    DP[T[0][0]][0] = T[0][1]
    for i in range(1, n):
        for j in range(E+1):
            if j+D[i]-D[i-1]<=E:
                DP[i][j] = min(DP[i][j], DP[i-1][j+D[i]-D[i-1]])
            if j>=1:
                DP[i][j] = min(DP[i][j], DP[i][j-1]+C[i])
        if T[i][0]>i:
            DP[T[i][0]][0] = min(DP[T[i][0]][0], DP[i][0]+T[i][1])
    return DP[n-1][0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
