class LRUCache:

    def __init__(self, capacity: int):
        self.lru_cache = OrderedDict()
        self.capacity = capacity
 
    def get(self, key: int) -> int:
        value = self.lru_cache.get(key,-1)
        if value != -1:
            self.lru_cache.move_to_end(key, last=True)
        return value

    def put(self, key: int, value: int) -> None:
        length = len(self.lru_cache)
        if length == self.capacity and key not in self.lru_cache:
            least_used = self.lru_cache.popitem(last=False)
        self.lru_cache[key] = value
        self.lru_cache.move_to_end(key, last=True)
