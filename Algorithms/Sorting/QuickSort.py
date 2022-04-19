"Quick Sort Implementation"



def QuickSort(array:list, leftHandIterator:int, rightHandIterator:int)->None:
    "while providing the righHandIterator which is basically highest or last element of list provide it as len(array) - 1"
    if leftHandIterator < rightHandIterator:
        # until leftHandIterator hasnt crossed or overlapped righthandIterator 
        # partition the array in two subarray using partition method 
        partitionPoint = Parition(array, leftHandIterator, rightHandIterator)

        # apply quick sort on subarray left of the partition point
        QuickSort(array, leftHandIterator, partitionPoint-1)
        # apply quick sort on subarray right of the partition point
        QuickSort(array, partitionPoint+1, rightHandIterator)

def Swap(array:list, index_1:int, index_2:int)->None:
    if index_1!=index_2:
        aux = array[index_1]
        array[index_1] = array[index_2]
        array[index_2] = aux

def Parition(array:list, leftHandIterator:int, rightHandIterator:int)->int:
    # store initial pivotIndex and pivot element
    pivotIndex = leftHandIterator
    pivot = array[pivotIndex]

    while leftHandIterator < rightHandIterator:
        # # until leftHandIterator hasnt crossed or overlapped righthandIterator
        while leftHandIterator < rightHandIterator and array[leftHandIterator] <= pivot:
            # if leftHandIterator has not crossed or overlapped the rightHandIterator
            # and value at leftHandIterator is less or equal to pivot then keep moving leftHandIterator to the right
            leftHandIterator += 1

        while array[rightHandIterator] > pivot:
            # value at rightHandIterator is greater than or equal to pivot then keep moving rightHandIterator to the left
            rightHandIterator -= 1

        if leftHandIterator < rightHandIterator:
            # if leftHandIterator less than rightHandIterator and the value at leftHandIterator is bigger than pivot as well as value at rightHandIterator is smaller then pivot,  then swap the values at both indexes
            Swap(array, leftHandIterator, rightHandIterator)

    # now after swapping the values after the iterations we need to put the pivot at correct position by swapping it with the value at rightHandIterator as it is smaller than pivot
    Swap(array, pivotIndex, rightHandIterator)

    return rightHandIterator