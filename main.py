import my_library as my

def main():
    lista = [1,5,2,1,7,11,2,9,1]
    print("Standard",lista)
    sortedBubble = my.bubble_sort(lista)
    print("Bubble: ",sortedBubble)
    sortedInsertion = my.insertion_sort(lista)
    print("Insertion",sortedInsertion)
    sortedSelection = my.selection_sort(lista)
    print("Selection", sortedSelection)
    sortedQuick = my.quick_sort(lista)
    print("Quick", sortedQuick)
    sortedHeap = my.heap_sort(lista)
    print("Heap", sortedHeap)
    sortedCouting = my.counting_sort(lista)
    print("Couting", sortedCouting)

if __name__ == "__main__":
    main()