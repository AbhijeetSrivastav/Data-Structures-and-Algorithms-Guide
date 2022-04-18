"Merge Sort Implementation"



def MergeSort(array)->list:
    # dividing the array into two unsorted array from mid until no element remain in array
    # namel leftHalf and rightHalf
    if len(array) > 1:
        "Divide"
        mid = len(array) // 2
        leftHalf = array[:mid]  #excluding mid(0 to mid)
        rightHalf = array[mid:] #including mid(mid to last)
        # similarly dividing the leftHalf first and then divide rightHalf
        MergeSort(leftHalf)
        MergeSort(rightHalf) 

        "Conqueor"
        # now merge all the divided subarrays 
        # array with one element is considerd sorted
        # declaring the iterator for leftHalf, rightHalf subarray and original array 
        leftHalfIterator = rightHalfIterator = arrayIterator = 0
        while leftHalfIterator < len(leftHalf) and rightHalfIterator < len(rightHalf):
            # loop untill in leftHalf and rightHalf
            if leftHalf[leftHalfIterator] > rightHalf[rightHalfIterator]:
                # if leftHalf element smaller than rightHalf 
                array[arrayIterator] = rightHalf[rightHalfIterator]
                rightHalfIterator += 1
                arrayIterator += 1
            elif leftHalf[leftHalfIterator] < rightHalf[rightHalfIterator]:
                # if rightHalf element smaller than leftHalf
                array[arrayIterator] = leftHalf[leftHalfIterator]
                leftHalfIterator += 1
                arrayIterator += 1
            else:
                # if the element of leftHalf and righHalf same
                array[arrayIterator] = leftHalf[leftHalfIterator]
                array[arrayIterator + 1] = rightHalf[rightHalfIterator]
                leftHalfIterator += 1
                rightHalfIterator += 1
                arrayIterator += 1

    return array


a = [2,8,6,3,7]
print(MergeSort(a))