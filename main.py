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
        print(obj.original_dict())
    #END ADAPTER




if __name__ == "__main__":
    main()