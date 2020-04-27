import my_library as my

def main():
    lista = [1,5,2,1,7,12,2,9,1]
    print("Standard",lista)

    sortedBubble = my.bubble_sort(lista)
    print("Bubble: ",sortedBubble)

    lista = [1, 5, 2, 1, 7, 12, 2, 9, 1]
    sortedInsertion = my.insertion_sort(lista)
    print("Insertion",sortedInsertion)

    lista = [1, 5, 2, 1, 7, 12, 2, 9, 1]
    sortedSelection = my.selection_sort(lista)
    print("Selection", sortedSelection)

    lista = [1, 5, 2, 1, 7, 12, 2, 9, 1]
    sortedQuick = my.quick_sort(lista)
    print("Quick", sortedQuick)

    lista = [1, 5, 2, 1, 7, 12, 2, 9, 1]
    sortedHeap = my.heap_sort(lista)
    print("Heap", sortedHeap)

    lista = [1, 5, 2, 1, 7, 12, 2, 9, 1]
    sortedCouting = my.counting_sort(lista,15)
    print("Couting", sortedCouting)

    lista = [1, 5, 2, 1, 7, 12, 2, 9, 1]
    sortedMerge = my.merge_sort(lista)
    print("Merge", sortedMerge)

if __name__ == "__main__":
    main()