from sortedcontainers import SortedList

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = SortedList()
        self.memory = {}
        self.index = 0

    def get(self, key: int) -> int:
        r = self.memory.get(key)
        if r:
            (value, c) = r
            self.lru.remove(c)
            c = (c[0] + 1, self.index, key)
            self.lru.add(c)
            self.memory[key] = (value, c)
            self.index += 1
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:        
        if self.capacity == 0:
            return

        if key in self.memory:
            (old_value, c) = self.memory[key]
            self.lru.remove(c)
            c = (c[0] + 1, self.index, key)
            self.lru.add(c)
            self.memory[key] = (value, c)
        else:
            if len(self.lru) == self.capacity and len(self.lru) > 0:
                (frequency, index, remove_key) = self.lru.pop(0)
                del self.memory[remove_key]

            c = (1, self.index, key)
            self.lru.add(c)
            self.memory[key] = (value, c)

        self.index += 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)