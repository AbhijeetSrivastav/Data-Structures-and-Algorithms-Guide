"Hash Table - with Seperate chaining collision resolution technique"



class HashTable:
    def __init__(self) -> None:
        self.MAX = 256

        # empty hash table with lists as elements
        # these lists act as chained lists
        # which stores multiple (key, value) tuple when collision happens
        self.array = [[] for i in range(self.MAX)]


    def getHash(self, key: str)->int:
        # Generate hash value for given value or maps value to index
        # hash = sum of the ASCII values of each char of key divided by the size of the hash table
        # ord is method to get ASCII value for a charachter
        hash = 0
        for char in key:
            hash += ord(char)
        hash = hash % self.MAX
        return hash

    def __setitem__(self, key:str, value)->None:
        # adds new key,value pair to chained list of the hash table
        h = self.getHash(key)
        found = False
        # idx is to get right position in chained list
        # element is to get the right tuple
        for idx, element in enumerate(self.array[h]):
            # loop over the chained list for tuples
            if len(element) == 2 and element[0] == key:
                # if len of tuple is two its valid and 
                # if first element of that tuple which is key 
                # is same as what we are trying to add
                self.array[h][idx] = (key, value)
                found = True
        if not found:
            # if key,value pair not found add it at appropriate hash value
            self.array[h].append((key, value))

    def __getitem__(self, key:str):
        # returns the value at given key
        h = self.getHash(key)
        for kv in self.array[h]:
            # loop over the appropriate chained list for key,value pair
            if kv[0] == key:
                # if found 
                return kv[1]

    def __delitem__(self, key:str)->None:
        # deletes key,value pair for given key from the hash table
        h = self.getHash(key)
        for idx, kv in enumerate(self.array[h]):
            if kv[0] == key:
                del self.array[h][idx]