"Shell Sort or Diminshing Insertion Sort or N-Gap Insertion Sort Implementation"



def ShellSort(array:list)->list:
    # gap within the elements to be compared
    gap = len(array) // 2
    
    while gap > 0:
        # while gap is valid keep doing these stuff
        for i in range(gap, len(array)):
            # looping over whole array to get the anchor at each gap 
            anchor = array[i]

            # j is the index of the last element of the sorted array which is on the left side of the original array with the anchor element as its first element
            j = i

            while j >= gap and array[j - gap] > anchor:
                # looping over the sorted array in reverse order from last to first 
                # sorted array is dispersed as its all elements are at gap in original array
                # the index of the first element is gap thats why termination condition is j >= gap
                # after that if the anchor element is smaller than current element in sorted array at left while reverse looping over it 
                # then we shift it and reduce our sorted array gap
                array[j] = array[j - gap]
                j -= gap
           
            array[j] = anchor
        # reduce the gap for next pass
        gap = gap // 2

    return array