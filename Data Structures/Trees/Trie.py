"Trie or Prefix Tree Implementation"



class Node:
    def __init__(self):
        # data will stored as key (charachters of text)
        # next node pointer will be stored as value of that key
        self.children = {}
        self.endofText = False

class Trie:
    def __init__(self):
        # initialize the first or root node
        self.root = Node()


    def insertText(self, text:str)->None:
        
        # point to the root node
        ptr = self.root

        # for each charachter of text
        for character in text:
            if character not in ptr.children:
                # if charachter not in children dictionary of current pointed node
                # insert that charachter and point it to new node
                ptr.children[character] = Node()
            
            # if charachter in children dictionary of current pointed node
            # move the pointer to that node
            ptr = ptr.children[character]
        
        # now its end of the text so set boolean
        ptr.endofText = True

    def searchText(self, text:str)->bool:
        "This method search whole tree for the text"
        # point to the root node
        ptr = self.root

        # for each charachter of text
        for charachter in text:
            # if charachter not in children dictionary of current pointed node
            # thus no text with this starting charachter exist
            if charachter not in ptr.children:
                return False

            # move the pointer to that node
            ptr = ptr.children[charachter]

        # is it end of the text ?
        if ptr.endofText:
            return True
        else: return False

    def startWith(self, text: str)->bool:
        "This method just checks wheter a text with a starting charchter exist or not"
        # point to the root node
        ptr = self.root

        # for each charachter of text
        for charchter in text:
            # if charachter not in children dictionary of current pointed node
            # thus no text with this starting charachter exist
            if charchter not in ptr.children:
                return False
            # move the pointer to that node
            ptr = ptr.children[charchter]

        # if exist return true
        return True