def merge(tab1, tab2):
    tabwynik = []
    i=j=0
    while i<len(tab1) and j<len(tab2):
        if tab1[i]<tab2[j]:
            tabwynik.append(tab1[i])
            i += 1
        else:
            tabwynik.append(tab2[j])
            j += 1
    if i>=len(tab1):
        while j<len(tab2):
            tabwynik.append(tab2[j])
            j += 1
    else:
        while i<len(tab1):
            tabwynik.append(tab1[i])
            i += 1
    return tabwynik

def msort(tab):
    n = len(tab)
    if n<=1:
        return tab
    mid = n//2
    left = msort(tab[:mid])
    right = msort(tab[mid:])
    return merge(left, right)


if __name__=="__main__":
    tab = [0, 9, 2, 4, 8, 3, 1, 0, 2, 2, 2, 3, 1231, 123, 213, 213123, 12]
    print(msort(tab))