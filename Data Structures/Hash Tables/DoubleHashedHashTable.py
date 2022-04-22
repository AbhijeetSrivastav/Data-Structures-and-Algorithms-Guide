"Hash Table - with Double Hashing collision resolution technique"



class HashTable:
    def __init__(self) -> None:
        self.MAX = 256

        # empty hash table with None value
        self.array = [None for i in range(self.MAX)]


    def getHash_1(self, key: str)->int:
        # Generate hash value for given value or maps value to index
        # hash = sum of the ASCII values of each char of key divided by the size of the hash table
        # ord is method to get ASCII value for a charachter
        hash = 0
        for char in key:
            hash += ord(char)
        hash = hash % self.MAX
        return hash
    
    def getHash_2(self, key:str)->int:
        # Generate hash value fpr given value or maps value to index
        # hash function is of your choice
        # here my hash function just does this
        # hash = (getHash_1() + 10) % self.MAX
        hash =  (self.getHash_1(key) + 10) % self.MAX
        return hash

    def __setitem__(self, key:str, value)->None:
        # adds new value to hash table
        # updates the value in the array at hash value for given key
        h = self.getHash_1(key)

        # iterator for quadratic function
        k = 1
        while self.array[h] is not None:
            # if the slot at hashed value is already occupied
            # rehash using the double hashing
            # that is we use two hash functions
            # first of all we just hash using first hash function and if it fails then only we start using both hash functions
            # rehash(key) = (hash_1(key) + hash_2(key)) + (hash_1(key) + k* hash_2(key))     
            h = self.getHash_1(key) + k * self.getHash_2(key)
            k += 1
        self.array[h] = value

    def __getitem__(self, key:str):
        # returns the value at given key
        h = self.getHash_1(key)
        return self.array[h]

    def __delitem__(self, key:str)->None:
        # deletes value for given key from the hash table
        h = self.getHash_1(key)
        self.array[h] = None