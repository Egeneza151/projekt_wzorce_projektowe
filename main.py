import my_library as my

def main():
    lista = [1,5,2,1,7,'abc',2,9,1]
    print("Standard",lista)

    sortedBubble = my.BubbleSort(lista)
    print("Bubble: ",sortedBubble.asc())

    lista = [1, 5, 2, 1, 7, 12, 2, 9, 1]
    sortedInsertion = my.InsertionSort(lista)
    print("Insertion",sortedInsertion.asc())

    lista = [1, 5, 2, 1, 7, 12, 2, 9, 1]
    sortedSelection = my.SelectionSort(lista)
    print("Selection", sortedSelection.asc())

    lista = [1, 5, 2, 1, 7, 12, 2, 9, 1]
    sortedQuick = my.QuickSort(lista)
    print("Quick", sortedQuick.asc())

    lista = [1, 5, 2, 1, 7, 12, 2, 9, 1]
    sortedHeap = my.HeapSort(lista)
    print("Heap", sortedHeap.asc())

    lista = [1, 5, 2, 1, 7, 12, 2, 9, 1]
    sortedCouting = my.CoutingSort(lista,15)
    print("Couting", sortedCouting.asc())

    lista = [1, 5, 2, 1, 7, 12, 2, 9, 1]
    sortedMerge = my.MergeSort(lista)
    #sortedMerge = my.malejaco(sortedMerge)
    print("Merge", sortedMerge.asc())

    #TWORZENIE OBSERWATOROW
    view1 = my.DecimalViewer()
    view2 = my.HexViewer()
    view3 = my.OctalViewer()

    #OBSERWATOR
    print("Obserwator")
    sortedBubble.attach(view1)#dodanie do obserwatora
    sortedBubble.attach(view2)
    sortedInsertion.attach(view1)
    sortedInsertion.attach(view2)
    sortedInsertion.attach(view3)
    sortedInsertion.detach(view1)#usuniecie z obserwatora
    sortedBubble.notify()#wyswietlenie obserwatora
    sortedInsertion.notify()
    #END OBSERWATOR

    #ADAPTER
    objects = []
    objects.append(my.Adapter(sortedBubble))
    objects.append(my.Adapter(sortedInsertion))
    objects.append(my.Adapter(sortedSelection))
    objects.append(my.Adapter(sortedQuick))
    print("Listy w klasie adapter:")
    for obj in objects:
        print("{0}".format(obj.tab))
        print("Właściwości",obj.original_dict())
    #END ADAPTER

    #FASADA
    fasada = my.SortingTime(lista, 15)
    fasada.show_time()
    #END FASADA

    #ALGORYTMY ARYTMETYCZNE
    alg_arytm = my.AlgorytmyArytmetyczne()
    silnia_rek = alg_arytm.silnia_rek(20)
    print(silnia_rek)
    silnia_iter = alg_arytm.silnia_iter(20)
    print(silnia_iter)
    fibo = alg_arytm.fib(10)
    print(fibo)
    nws1 = alg_arytm.nws_v1(10,15)
    print(nws1)
    nws2 = alg_arytm.nws_v2(10, 15)
    print(nws2)
    nww = alg_arytm.nww(10, 15)
    print(nww)
    sito = alg_arytm.sito(100)
    print(sito)
    fme = alg_arytm.fme(3, 2, 3)#fast modular exponentiation
    print(fme)
    rozklad = alg_arytm.rozklad(2136)
    print(rozklad)
    newton = alg_arytm.Newton(40, 37)
    print(newton)
    #print(fermat)
    #END ALGORYTMY ARYTMETYCZNE

    #BUILDER
    lista_to_build = [2,1,3,7,8,4,2,1]
    director = my.DirectorBuilder(lista_to_build, 100)
    builder = my.SortBuilder()
    director.builder = builder

    director.build_sorting()
    #director.build_random()
    print(builder.counting_sort.asc())
    #END BUILDER



if __name__ == "__main__":
    main()