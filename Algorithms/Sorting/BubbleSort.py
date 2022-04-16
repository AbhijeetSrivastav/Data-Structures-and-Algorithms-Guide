"Bubble Sort (Sinking Sort) Implementation"



def BubbleSort(array:list)->list:
    for j in range(len(array)):
        # looping to acess each element of the array
        for i in range(0, len(array) - 1):
            # looping for each pass to compare the ith and i+1th element
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


def OptimizedBubbleSort(array:list)->list:
    for j in range(len(array)):
        # looping to acess each element of the array

        # keep track of swapping
        swapped = False
        
        for i in range(0, len(array) - 1):
            # looping for each pass to compare the ith and i+1th element
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
            
        if not swapped:
            # this condition checked after each pass
            # this means array is already sorted
            break

    return array