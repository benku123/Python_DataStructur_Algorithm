class ChainingHashTable:
    def __init__(self, value):
        self.value = value
        self.array = [[] for _ in range(value)]

    def hash(self, keyvalue):
        hash_key = sum(ord(i) for i in keyvalue)
        index_in_array = hash_key % self.value
        self.array[index_in_array].append(keyvalue)

    def display_hashtable(self):
        for i in range(len(self.array)):
            print(i, end='')
            for j in self.array[i]:
                print('-->', end=j)
            print()


s = ChainingHashTable(10)
s.hash('hello')
s.hash('good')
s.hash('Abracadabra')
s.hash('Poter')
s.display_hashtable()

