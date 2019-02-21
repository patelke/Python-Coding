def quicksort(array):
    first = 0
    last = len(array)-1
    _quicksort(array,first,last)

def _quicksort(array,first,last):
    if first<last:
        pivot_idx = partition(array,first,last)
        _quicksort(array,first,pivot_idx-1)
        _quicksort(array, pivot_idx + 1, last)

def partition(array,first,last):
    idx = first
    pivot = array[last]
    for j in range(first,last):
        if array[j]<= pivot:
            swap(array,j,idx)
            idx += 1
    swap(array,idx,last)
    return idx



def swap(array,idx_1,idx_2):
    array[idx_1],array[idx_2] = array[idx_2],array[idx_1]



if __name__ == "__main__":
    from random import shuffle
    myList = [i for i in range(50)]
    shuffle(myList)
    quicksort(myList)
    print(myList)
