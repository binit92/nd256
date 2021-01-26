from collections import OrderedDict

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.cache or len(self.cache) == self.capacity:
            #print("get",-1)
            return -1
        else:
            self.cache.move_to_end(key)
            #print("get",self.cache[key])
            return self.cache[key]

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if len(self.cache) == self.capacity:
            self.cache.popitem(last = True)
        self.cache[key] = value
        self.cache.move_to_end(key)

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
