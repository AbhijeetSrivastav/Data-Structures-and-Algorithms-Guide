"Insertion Sort Implementation"



def InsertionSort(array:list)->list:
    for i in range(1, len(array)):
        # looping over whole array to get the anchor at each iteration 
        anchor = array[i]

        # j is the index of the last element of the sorted array which is on the left side of the original array with the anchor element as its first element
        j = i - 1

        while j >= 0 and anchor < array[j]:
            # looping over the sorted array in reverse order from last to first 
            # the index of the first element is 0 thats why termination condition is j >= 0
            # after that if the anchor element is smaller than current element in sorted array at left while reverse looping over it 
            # then we shift it and reduce our sorted array iterator
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = anchor

    return array  