def bubblesort(array):
    swapped = True
    count = 0
    while swapped == True:
        count += 1
        swapped = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i],array[i+1] = array[i+1],array[i]
                swapped = True
    print("Count ", count)

def insertionsort(array):
    for i in range(len(array)):
        if i > 0:
            val = array[i]
            for j in range(i,-1,-1):
                if val < array[j-1]:
                    array[j] = array[j-1]
                else:
                    break
            array[j] = val

def selectionsort(array):
    for i in range(len(array)):
        smallest_idx = i
        for j in range(i,len(array)):
            if array[j]<array[smallest_idx] :
                smallest_idx = j
        array[i],array[smallest_idx] = array[smallest_idx],array[i]





if __name__ == "__main__":
    from random import shuffle
    myList = [i for i in range(6)]
    shuffle(myList)
    print(myList)
    insertionsort(myList)
    print(myList)