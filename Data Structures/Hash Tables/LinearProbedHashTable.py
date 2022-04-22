"Hash Table - with Linear Probing collision resolution technique"



class HashTable:
    def __init__(self) -> None:
        self.MAX = 256

        # empty hash table with None value
        self.array = [None for i in range(self.MAX)]


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
        # adds new value to hash table
        # updates the value in the array at hash value for given key
        h = self.getHash(key)
       
        if self.array[h] is not None:
            # if the slot at hashed value is already occupied
            # rehash using the linear probe
            # rehash(key) = (hash + 1) % size_of_table
            h = (h + 1) % self.MAX
        self.array[h] = value

    def __getitem__(self, key:str):
        # returns the value at given key
        h = self.getHash(key)
        return self.array[h]

    def __delitem__(self, key:str)->None:
        # deletes value for given key from the hash table
        h = self.getHash(key)
        self.array[h] = None