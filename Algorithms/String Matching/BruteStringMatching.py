"Brute force Implementation for String Matching"



def BrutePatternMatch(text:str, pattern:str)->int:
    LT = len(text)
    LP = len(pattern)

    # max index at which pattern matching can start before exceeding the length of the text
    MAX = LT - LP + 1       

    for ti in range(0, MAX):
        # looping in text to put the pattern at correct index to be matched
        pi = 0
        while ti < LT and pi < LP and text[ti] == pattern[pi]:
            # looping in pattern to compare charachter in pattern
            # with charachter in text
            ti += 1
            pi += 1
        if pi == LP: return ti
    return -1