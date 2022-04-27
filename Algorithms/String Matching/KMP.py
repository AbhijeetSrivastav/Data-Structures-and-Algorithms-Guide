"Knuth Morris and Prath (KMP) Implementation for String Matching"



def KMP(pattern:str, text:str)->int:
    patternLength = len(pattern)
    textLength = len(text)

    prefixTable = computePrefixTable(pattern, patternLength)

    initialPoint = []
    m = 0
    n = 0

    # matching the chacrachters of pattern with text
    while m != textLength:
        if text[m] == pattern[n]:
            m += 1
            n += 1
        else:
            n = prefixTable[n-1]

        if n == patternLength:
            initialPoint.append(m-n)
            n = prefixTable[n-1]
        elif n == 0:
            m += 1
    return initialPoint

def computePrefixTable(pattern:str, patternLength:int)->list:
    prefixTable = [0] * patternLength
    n = 0
    m = 1

    # checking if elements repatation in pattern and saving the index at which it repats as value to prefixTable
    while m != patternLength:
        if pattern[m] == pattern[n]:
            n += 1
            prefixTable[m] = n
            m += 1
        elif n != 0:
            n = prefixTable[n- 1]
        else:
            prefixTable[m] = 0
            m += 1
    
    return prefixTable