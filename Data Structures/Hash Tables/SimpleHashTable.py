"Simple Hash Table - without Collision Resolution"


"""Naive Way: Here if you have to perform an action then you have to do it like this:
   t = HashTable()
   t.add('hello', 22)
   t.getItem('hello')
   t.delete('hello')
"""
class HashTable:
    def __init__(self) -> None:
        self.MAX = 256

        # empty hash table wit None value
        self.array = [None for i in range(self.MAX)]


    def getHash(self, key: str)->int:
        # Generate hash value for given value
        # or maps value to index
        # hash = sum of the ASCII values of each char of key divided by the size of the hash table
        # ord is method to get ASCII value for a charachter
        hash = 0
        for char in key:
            hash += ord(char)
        hash = hash % self.MAX
        return hash

    def add(self, key:str, value)->None:
        # adds new value to hash table
        # updates the value in the array at hash value for given key
        h = self.getHash(key)
        self.array[h] = value

    def getItem(self, key:str):
        # returns the value at given key
        h = self.getHash(key)
        return self.array[h]

    def delete(self, key:str)->None:
        # deletes value for given key from the hash table
        h = self.getHash(key)
        self.array[h] = None

"""Advance Way: Here we can use operators provided by python to make the operations more feasible like what we see with ADT like dictionary and now here you can perform actions like this:
   t = HashTable()
   t['hello'] = 12
   t['hello']
   del t['hello']
"""
class HashTable:
    def __init__(self) -> None:
        self.MAX = 256

        # empty hash table wit None value
        self.array = [None for i in range(self.MAX)]


    def getHash(self, key: str)->int:
        # Generate hash value for given value
        # or maps value to index
        # hash = sum of the ASCII values of each char of key divided by the size of the hash table
        # ord is method to get ASCII value for a charachter
        hash = 0
        for char in key:
            hash += ord(char)
        hash = hash % self.MAX
        return hash

    def __setitem__(self, key:str, value)->None:
        # adds new value to hash table
        # updates the value in the array at hash value for given key
        h = self.getHash(key)
        self.array[h] = value

    def __getitem__(self, key:str):
        # returns the value at given key
        h = self.getHash(key)
        return self.array[h]

    def __delitem__(self, key:str)->None:
        # deletes value for given key from the hash table
        h = self.getHash(key)
        self.array[h] = None