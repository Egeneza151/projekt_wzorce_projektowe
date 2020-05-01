import math
from abc import ABCMeta, abstractmethod

#KLASA ADAPTER - zapewnia inny interfejs dla klas(trzeba bedzie wykrzystac klasy niepowiazane ze soba)
class Adapter:
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__

#KLASA PRZODKA SORTOWANIA
class Sorting:
    def __init__(self):
        self._observers = []

    def asc(self):#rosnaco
        return self.tab

    def desc(self):#malejaco
        temp = []
        dl = len(self.tab)
        for i in range(0,dl):
            temp.append(self.tab[dl-i-1])
        return temp

    def isInteger(self, tab):#jesli w tablicy jest string zamienia go na 0
        for i in range(len(tab)):
            isString = type(tab[i]) == str
            if (isString == True):
                tab[i] = 0
        return tab

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

#KLASY SORTOWANIA
class BubbleSort(Sorting):
    def __init__(self, tab):
        Sorting.__init__(self)
        self.tab = tab
        self.tab = self.isInteger(self.tab)
        self.tab = self.bubble_sort(self.tab)

    def bubble_sort(self, tab): #zwraca posortowaną tablicę
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


class InsertionSort(Sorting):
    def __init__(self, tab):
        Sorting.__init__(self)
        self.tab = tab
        self.tab = self.isInteger(self.tab)
        self.tab = self.insertion_sort(self.tab)

    def insertion_sort(self,tab):
        """Sortowanie przez wstawianie"""
        # dla kolejnych elementow
        for i in range(1, len(tab)):
            key = tab[i]
            j = 0
            # poszukaj miejsce gdzie wstawic aktualny element
            while key > tab[j] and j < i:
                j += 1
            tab.insert(j, key)  # wstaw element w znalezione miejsce
            del tab[i + 1]  # usun element - wstawilismy element na miejsce (stworzylismy jego kopie, usun oryginal)
        return tab


class SelectionSort(Sorting):
    def __init__(self, tab):
        Sorting.__init__(self)
        self.tab = tab
        self.tab = self.isInteger(self.tab)
        self.tab = self.selection_sort(self.tab)

    def selection_sort(self, tab):
        """Sortowanie przez wymiane/wybor"""
        for i, n in enumerate(tab):
            j, m = min(enumerate(tab[i:]), key = lambda a: a[1])
            tab[j + i], tab[i] = n, m
        return tab


class QuickSort(Sorting):
    def __init__(self, tab):
        Sorting.__init__(self)
        self.tab = tab
        self.tab = self.isInteger(self.tab)
        self.tab = self.quick_sort(self.tab)

    def quick_sort(self, tab):
        """Sortowanie szybkie"""
        if len(tab) <= 1:
            return tab
            # pobieranie pivota wg ktorego bedzimey operowac
        pivot = tab[0]
        less = []

        # wszystkie mniejsze elementy od pivot przerzucamy do listy mniejszych
        for x in tab:
            if x < pivot:
                less.append(x)

        # wszystkie rowne elementy przerzucamy do listy rownych
        equal = []
        for x in tab:
            if x == pivot:
                equal.append(x)

        # wszystkie wiesze elementy od pivot przerzucamy do listy wiekszych
        greater = []
        for x in tab:
            if x > pivot:
                greater.append(x)

        # (rekurencja) odnawiamy procedure dla mniejszych i wiekszych elementow
        return self.quick_sort(less) + equal + self.quick_sort(greater)


class HeapSort(Sorting):
    def __init__(self, tab):
        Sorting.__init__(self)
        self.tab = tab
        self.tab = self.isInteger(self.tab)
        self.tab = self.heap_sort(self.tab)

    def heap_sort(self, tab):
        """Sortowanie stogowe"""
        # budowanie kopca
        #print("[LOG] Budowanie kopca")
        for start in range(int((len(tab) - 2) / 2), -1, -1):
            self.shiftdown(tab, start, len(tab) - 1)

        # sortowanie
        for end in range(len(tab) - 1, 0, -1):
            #print("[LOG] Zamiana: " + str(L[end]) + " z " + str(L[0]))
            tab[end], tab[0] = tab[0], tab[end]  # swap
            self.shiftdown(tab, 0, end - 1)  # przywracanie wlasnosci kopca
        return tab

    # spusc element pod indeksem start w dol - tak by byl zachowany warunek kopca
    def shiftdown(self, lst, start, end):
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


class CoutingSort(Sorting):
    def __init__(self, tab, maxValue):
        Sorting.__init__(self)
        self.tab = tab
        self.maxValue = maxValue
        self.tab = self.isInteger(self.tab)
        self.tab = self.counting_sort(self.tab, self.maxValue)

    def counting_sort(self, tab, maxValue):
        """Sortowanie przez zliczanie"""
        size = len(tab)
        output = [0] * size

        # Initialize count array
        count = [0] * maxValue

        # Store the count of each elements in count array
        for i in range(0, size):
            count[tab[i]] += 1

        # Store the cummulative count
        for i in range(1, maxValue):
            count[i] += count[i - 1]

        # Find the index of each element of the original array in count array
        # place the elements in output array
        i = size - 1
        while i >= 0:
            output[count[tab[i]] - 1] = tab[i]
            count[tab[i]] -= 1
            i -= 1

        # Copy the sorted elements into original array
        for i in range(0, size):
            tab[i] = output[i]
        return tab


class MergeSort(Sorting):
    def __init__(self, tab, zakres = 0):
        Sorting.__init__(self)
        self.tab = tab
        self.tab = self.isInteger(self.tab)
        self.tab = self.merge_sort(self.tab)

    def merge(self, tab, start, center, finish):
        """Operacja scalania"""
        i = start
        j = center + 1
        tab2 = []  # lista pomocnicza
        # wybieraj odpowiednie elementy z dwoch tablic
        while (i <= center) and (j <= finish):
            if tab[j] < tab[i]:
                tab2.append(tab[j])
                j = j + 1
            else:
                tab2.append(tab[i])
                i = i + 1

        # jedna z tablic skonczyla sie przepisz reszte z pozostalej
        if i <= center:
            while i <= center:
                tab2.append(tab[i])
                i = i + 1
        else:
            while j <= finish:
                tab2.append(tab[j])
                j = j + 1

        # przepisz wyniki z tablicy tymczasowej
        s = finish - start + 1
        i = 0
        while i < s:
            tab[start + i] = tab2[i]
            i = i + 1
        return tab

    # sortowanie przez scalanie
    def merge_me(self, tab, start, finish):
        """Rekruencyjne scalanie"""
        if start != finish:
            # dzielimy dablice do konca
            center = int(math.floor((start + finish) / 2))
            # na lewo
            self.merge_me(tab, start, center)
            # na prawo
            self.merge_me(tab, center + 1, finish)

            # operacja scalania
            self.merge(tab, start, center, finish)
        return tab

    def merge_sort(self, tab, zakres = 0):
        """Sortowanie przez scalanie"""
        if zakres != 0:
            dl = zakres
        else:
            dl = len(tab)
            dl = dl - 1
        return self.merge_me(tab,0,dl)
#END KLASY SORTOWANIA
#OBSERWATORZY
class HexViewer:
    def update(self, sorting):
        print("HEX VIEWER:",[hex(x) for x in sorting.tab])


class DecimalViewer:
    def update(self, sorting):
        print("DECIMAL VIEWER:",sorting.tab)


class OctalViewer:
    def update(self, sorting):
        print("OCTAL VIEWER:",[oct(x) for x in sorting.tab])
#END OBSERWATORZY

#ADD: Obserwer - zbieranie logow z uzywania algorytmow
#ADD Fasada - dzielenie logiki od biznesu(w tym przypadku wywolanie jakiejs prywatnej metody)