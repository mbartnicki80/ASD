from random import randint

def median(tab):
    for i in range(len(tab)):
        for j in range(1, len(tab)-i):
            if tab[j]<tab[j-1]:
                tab[j], tab[j-1] = tab[j-1], tab[j]
    return tab[len(tab)//2]
        

def partition(tab, l, r):
    medians = [median(tab[i:min(i+5, r+1)]) for i in range(l, r+1, 5)]
    if len(medians)<=5: 
        piv = median(medians)
    else: 
        piv = qs(medians, len(medians)//2, 0, len(medians)-1)
        
    ind = 0
    for i in range(l, r+1):
        if tab[i]==piv:
            ind = i
            break

    tab[r], tab[ind] = tab[ind], tab[r]
    i = l-1
    for j in range(l, r+1):
        if tab[j]<=piv:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    return i


def qs(tab, k, l, r):
    q = partition(tab, l, r)
    if q==k:
        return tab[q]
    elif q<k:
        return qs(tab, k, q+1, k)
    else:
        return qs(tab, k, l, q-1)

if __name__=="__main__":
    tab = [0, 2, 1, 123, 12, 123, 432, 6, 324, 13]
    print(qs(tab, 8, 0, len(tab)-1))
    print(sorted(tab))