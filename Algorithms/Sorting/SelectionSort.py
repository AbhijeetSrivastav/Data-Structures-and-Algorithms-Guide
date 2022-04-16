"Selection Sort Implementation"



def SelectionSort(array:list)->list:
    for i in range(len(array)-1):
        # looping over array to select an element as min at each iteration
        min_index = i
        for j in range(min_index+1,len(array)):
            # looping over the elements after the selected min element
            # comparing is their another min element in the remaining part of array
            if array[j] < array[min_index]:
                # if their is min element in remaining part of array 
                # update the index of the min element
                min_index = j

        # swap the min element with newly found min element
        array[i], array[min_index] = array[min_index], array[i]

    return array