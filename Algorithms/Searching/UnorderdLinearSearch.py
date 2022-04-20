"Unorderd Linear Search Implementation"



def UnorderdLinearSearch(array:list, searchForValue:int)->int:
    for _ in range(len(array)):
        if array[_] == searchForValue:
            return _
    return -1

a = [2,77,8,34,68,9,3,33,56,5]
print(UnorderdLinearSearch(a, 1))