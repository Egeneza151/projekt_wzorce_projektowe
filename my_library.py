import math

def bubble_sort(tab): #zwraca posortowaną tablicę
    """Sortowanie babelkowe"""
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
    """Sortowanie przez wstawianie"""
    # dla kolejnych elementow
    for i in range(1, len(data)):
        key = data[i]
        j = 0
        # poszukaj miejsce gdzie wstawic aktualny element
        while key > data[j] and j < i:
            j += 1
        data.insert(j, key)  # wstaw element w znalezione miejsce
        del data[i + 1]  # usun element - wstawilismy element na miejsce (stworzylismy jego kopie, usun oryginal)
    return data


def selection_sort(y):
    """Sortowanie przez wymiane/wybor"""
    for i, n in enumerate(y):
        j, m = min(enumerate(y[i:]), key = lambda a: a[1])
        y[j + i], y[i] = n, m
    return y


def quick_sort(L):
    """Sortowanie szybkie"""
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
    """Sortowanie stogowe"""
    # budowanie kopca
    #print("[LOG] Budowanie kopca")
    for start in range(int((len(L) - 2) / 2), -1, -1):
        shiftdown(L, start, len(L) - 1)

    # sortowanie
    for end in range(len(L) - 1, 0, -1):
        #print("[LOG] Zamiana: " + str(L[end]) + " z " + str(L[0]))
        L[end], L[0] = L[0], L[end]  # swap
        shiftdown(L, 0, end - 1)  # przywracanie wlasnosci kopca
    return L


# spusc element pod indeksem start w dol - tak by byl zachowany warunek kopca
def shiftdown(lst, start, end):
    """Metoda do produkcji kopca"""
    root = start
    #print("[LOG] Przywracanie wlasnosci kopca")
    #print("[LOG] Ustalamy korzen: " + str(root))
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


def counting_sort(array,maxValue):
    """Sortowanie przez zliczanie"""
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * maxValue

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cummulative count
    for i in range(1, maxValue):
        count[i] += count[i - 1]

    # Find the index of each element of the original array in count array
    # place the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]
    return array


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
def merge_me(L, start, finish):
    """Rekruencyjne scalanie"""
    if start != finish:
        # dzielimy dablice do konca
        center = int(math.floor((start + finish) / 2))
        # na lewo
        merge_me(L, start, center)
        # na prawo
        merge_me(L, center + 1, finish)

        # operacja scalania
        merge(L, start, center, finish)
    return L


def merge_sort(L, zakres = 0):
    """Sortowanie przez scalanie"""
    if zakres != 0:
        dl = zakres
    else:
        dl = len(L)
        dl = dl - 1
    return merge_me(L,0,dl)


def malejaco(n):#DONE - quick, heap, counting, merge TODO: bubble, insertion, selection
    L = []
    for i in range(0,n):
        L.append(n-i-1)
    return L
