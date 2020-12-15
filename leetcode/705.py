import numpy
import typing

class MyHashSet:
    TABLE_SIZE = 500

    def __init__(self):
        hash_table = None
        self.make()

    def make(self) -> None:
        self.hash_table = [ [] for _ in range(self.TABLE_SIZE) ]

    def index(self, key: int) -> int:
        return key % self.TABLE_SIZE

    def add(self, key: int) -> None:
        index = self.index(key)
        if key not in self.hash_table[index]:
            self.hash_table[index].append(key)

    def remove(self, key: int) -> None:
        index = self.index(key)
        if key in self.hash_table[index]:
            self.hash_table[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self.index(key)
        if key in self.hash_table[index]:
            return True
        return False
    
class Main:
    def execute(self):
        my_hash_set = MyHashSet()

        my_hash_set.add(1)
        my_hash_set.add(2)
        print(my_hash_set.contains(1))
        print(my_hash_set.contains(3))
        my_hash_set.add(2)
        print(my_hash_set.contains(2))
        my_hash_set.remove(2)
        print(my_hash_set.contains(2))
        
main = Main()
main.execute()

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)