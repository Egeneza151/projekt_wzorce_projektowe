



def bubble_sort(tab): #zwraca posortowaną tablicę
    for i in range(len(tab)):
        j=len(tab)-1 #od ostatniej komórki
        while j>i:   #do aktualnie szukanej jako najmniejsza
            if tab[j]<tab[j-1]: #jeśli komórka wcześniej jest mniejsza, zamienia
                tmp=tab[j]
                tab[j]=tab[j-1]
                tab[j-1]=tmp
            j-=1
    return tab




def insertion_sort(data):
    #dla kolejnych elementow
    for i in range(1, len(data)):
        key = data[i]
        j = 0
        #poszukaj miejsce gdzie wstawic aktualny element
        while key > data[j] and j<i:
            j += 1
        data.insert(j, key) #wstaw element w znalezione miejsce
        del data[i+1] #usun element - wstawilismy element na miejsce (stworzylismy jego kopie, usun oryginal)

def selection_sort(y):
    for i, n in enumerate(y):
        j, m = min(enumerate(y[i:]), key = lambda a: a[1])
        y[j + i], y[i] = n, m
    return y    #example:print selection_sort([2,6,1,9,4,3]);




def quick_sort(L):
    if len(L) <= 1:
        return L
        # pobieranie pivota wg ktorego bedzimey operowac
    pivot = L[0]
    less = []

    # wszystkie mniejsze elementy od pivot przerzucamy do listy mniejszych
    for x in L:
        if x < pivot:
            less.append(x)

    # wszystkie rowne elementy przerzucamy do listy rownych
    equal = []
    for x in L:
        if x == pivot:
            equal.append(x)

    # wszystkie wiesze elementy od pivot przerzucamy do listy wiekszych
    greater = []
    for x in L:
        if x > pivot:
            greater.append(x)

    # (rekurencja) odnawiamy procedure dla mniejszych i wiekszych elementow
    return quick_sort(less) + equal + quick_sort(greater)





def heap_sort(L):
    """Sortowanie Heap sort"""

    # budowanie kopca
    print("[LOG] Budowanie kopca")
    for start in range(int((len(L) - 2) / 2), -1, -1):
        shiftdown(L, start, len(L) - 1)

    # sortowanie
    for end in range(len(L) - 1, 0, -1):
        print("[LOG] Zamiana: " + str(L[end]) + " z " + str(L[0]))
        L[end], L[0] = L[0], L[end]  # swap
        shiftdown(L, 0, end - 1)  # przywracanie wlasnosci kopca
    return L


# spusc element pod indeksem start w dol - tak by byl zachowany warunek kopca
def shiftdown(lst, start, end):
    """Metoda do produkcji kopca"""
    root = start
    print("[LOG] Przywracanie wlasnosci kopca")
    print("[LOG] Ustalamy korzen: " + str(root))
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break


def counting_sort(L):
    """Sortowanie counting sort"""
    tab_pom = []

    print("[LOG] Tworzenie tablicy pomocniczej")
    for i in range(0, len(L)):
        tab_pom.append(0);

    print("[LOG] zliczanie poszczegolnych lementow")
    for a in L:
        print("[LOG] zliczono element: " + str(a))
        tab_pom[a] = tab_pom[a] + 1

    print("[LOG] Ukladanie posortoanej tablicy")
    k = 0  # index tablicy
    for a in range(0, len(L)):
        for c in range(0, tab_pom[a]):
            L[k] = a
            k = k + 1
    return L





def merge(L, start, center, finish):
    """Operacja scalania"""
    i = start
    j = center + 1

    L2 = []  # lista pomocnicza

    # wybieraj odpowiednie elementy z dwoch tablic
    while (i <= center) and (j <= finish):
        if L[j] < L[i]:
            L2.append(L[j])
            j = j + 1
        else:
            L2.append(L[i])
            i = i + 1

    # jedna z tablic skonczyla sie przepisz reszte z pozostalej
    if i <= center:
        while i <= center:
            L2.append(L[i])
            i = i + 1
    else:
        while j <= finish:
            L2.append(L[j])
            j = j + 1

    # przepisz wyniki z tablicy tymczasowej
    s = finish - start + 1
    i = 0
    while i < s:
        L[start + i] = L2[i]
        i = i + 1

    return L


# sortowanie przez scalanie
def merge_sort(L, start, finish):
    """sortowanie merge sort"""
    if start != finish:
        # dzielimy dablice do konca
        center = int(math.floor((start + finish) / 2))
        # na lewo
        merge_sort(L, start, center)
        # na prawo
        merge_sort(L, center + 1, finish)

        # operacja scalania
        merge(L, start, center, finish)
    return L





def malejaco(n):#DONE - quick, heap, counting, merge TODO: bubble, insertion, selection
    L = []
    for i in range(0,n):
        L.append(n-i-1)
    return L
