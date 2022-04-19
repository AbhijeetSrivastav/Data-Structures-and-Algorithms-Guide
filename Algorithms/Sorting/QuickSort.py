"Quick Sort Implementation"



def QuickSort(array:list, leftHandIterator:int, rightHandIterator:int)->list:
    while leftHandIterator < rightHandIterator:
        partitionPoint = Partition(array, leftHandIterator, rightHandIterator)
        QuickSort(array, leftHandIterator, partitionPoint - 1)
        QuickSort(array, partitionPoint + 1, rightHandIterator)

def Partition(array: list, leftHandIterator:int, rightHandIterator:int)->list:
    pivot = array[0]

    leftHandIterator +=1
    rightHandIterator = rightHandIterator

    done = False

    while not done:
        while leftHandIterator <= rightHandIterator and array[leftHandIterator] <= pivot:
            leftHandIterator += 1
        
        while rightHandIterator >= leftHandIterator and array[rightHandIterator] >= pivot:
                rightHandIterator -= 1
        
        if rightHandIterator < leftHandIterator:
                done = True
        else:
            aux = array[leftHandIterator]
            array[leftHandIterator] = array[rightHandIterator]
            array[rightHandIterator] = aux
    
    return rightHandIterator


a = [2,5,7,9,8, 3, 0]
print(QuickSort(array=a, leftHandIterator=0, rightHandIterator=len(a)))