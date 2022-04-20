"Orderd Linear Search Implementation"



def OrderdLinearSearch(array: list, searchForValue:int)->int:
    for _ in range(len(array)):
        if array[_] == searchForValue:
            return _
        elif  array[_] > searchForValue:
            # as list is sorted thus if value become more than what are looking for, # then it will not be their in list
            return -1
    return -1