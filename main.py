import my_library as my

def main():
    lista = [1,5,2,1,7,12,2,9,1]
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

if __name__ == "__main__":
    main()