"Rabin Karp Algorithm for String Matching"



def RabinKarp(pattern:str, text:str, primeDivider:int)->int:
    patternLength = len(pattern)
    textLength = len(text)
    assumedTextLength = 10          # number of charachters in text (assumed) 
    patternHash = 0
    textHash = 0
    h = 1
    i = 0
    j = 0

    for i in range(patternLength-1):
        h = (h * assumedTextLength) % primeDivider

    # Calculate hash value for pattern and text
    for i in range(patternLength):
        patternHash = (assumedTextLength * patternHash + ord(pattern[i])) % primeDivider
        textHash = (assumedTextLength * textHash + ord(text[i])) % primeDivider

    # Find the match
    for i in range(textLength-patternLength + 1):
        if patternHash == textHash:
            # if pattern hash is equal to text hash in current window
            for j in range(patternLength):
                # loop over the pattern to check whether all the charachters match or not
                if text[i+j] != pattern[j]:
                    # if not match
                    break
            
            # if match
            j += 1
            if j == patternLength:
                return str(i+1)

        if i < textLength - patternLength:
            # calculating hash of text for the next window
            # by subtracting the hash of one element in front and subtracting one in rear
            # as window moves one element at time to the right
            textHash = (assumedTextLength * (textHash - ord(text[i]) * h) + ord(text[i + patternLength])) % primeDivider

            if textHash < 0:
                textHash = textHash + primeDivider