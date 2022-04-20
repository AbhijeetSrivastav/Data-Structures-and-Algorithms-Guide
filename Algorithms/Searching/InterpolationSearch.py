"Interpolation Search Implementation(Upgraded Binary Search)"



def InterpolationSearch(array:list, searchForValue:int)->int:
    low = 0
    high = len(array) - 1

    while array[low] <= searchForValue  <= array[high]:
        # formula for interpolation point
        mid = (low + (searchForValue - array[low]) * (high - low)) // (array[high] - array[low])

        if array[mid] > searchForValue:
            high = mid - 1
        elif array[mid] < searchForValue:
            low = mid + 1
        else:
            # array[mid] == searchForValue
            return mid
    
    return -1