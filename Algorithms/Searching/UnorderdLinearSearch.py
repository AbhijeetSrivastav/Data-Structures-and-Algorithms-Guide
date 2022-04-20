"Unorderd Linear Search Implementation"



def UnorderdLinearSearch(array:list, searchForValue:int)->int:
    for _ in range(len(array)):
        if array[_] == searchForValue:
            return _
    return -1