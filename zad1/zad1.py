from zad1testy import runtests
'''
Mateusz Bartnicki
Opis algorytmu:
Znajduję środkowy indeks, który będę jednocześnie rozsuwać w lewo i prawo w pętli for. Będzie to środek
szukanego palindromu. W pętlach while za pomocą pomocniczych zmiennych będę szukać, czy występuje
palindrom. Będę wykonywać pętlę, dopóki nie sprawdzę każdego indeksu, bądź nie dojdę do momentu,
w którym niemożliwym jest znalezienie dłuższego palindromu.
Szacowana zlozonosc obliczeniowa: O(n^2)
'''

def ceasar( s ):
    
    n = len(s)
    maksdl = 1
    sr = n//2

    for i in range(n//2):
        dlj = 1; dlk=1
        j = sr-i; k = sr+i

        if n-k+(n-k+1)<maksdl and 2*j+1<maksdl:
            break

        startj = j-1; stopj = j+1
        startk = k-1; stopk = k+1

        while (startj>=0 and stopj<=n-1 and s[startj]==s[stopj]):
            dlj += 2
            startj -= 1
            stopj += 1

        while (startk>=0 and stopk<=n-1 and s[startk]==s[stopk]):
            dlk += 2
            startk -= 1
            stopk += 1

        maksdl = max(max(dlj, dlk), maksdl)

    return maksdl

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
