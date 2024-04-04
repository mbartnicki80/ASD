from random import randint

def partition(tab, l, r):
    piv = randint(l, r)
    tab[piv], tab[r] = tab[r], tab[piv]
    q = tab[r]
    i = l-1
    for j in range(l, r):
        if tab[j]<=q:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[r], tab[i+1] = tab[i+1], tab[r]
    return i+1

def qsort(tab, l, r):
    while l<r:
        q = partition(tab, l, r)
        if r-q<q-l:
            qsort(tab, q+1, r)
            r = q-1
        else:
            qsort(tab, l, q-1)
            l = q+1
    return tab

if __name__=="__main__":
    tab = [0, 9, 2, 4, 8, 3, 1, 0, 2, 2, 2, 3, 1231, 123, 213, 213123, 12]
    print(qsort(tab, 0, len(tab)-1))