
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.nodes = {}
        self.freqs = {}

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        freq = node[1]

        del self.freqs[freq][key]

        if not self.freqs[freq]:
            del self.freqs[freq]
            if self.min_freq == freq:
                self.min_freq += 1

        node[1] += 1
        new_freq = node[1]

        if new_freq not in self.freqs:
            self.freqs[new_freq] = {}

        self.freqs[new_freq][key] = None
        return node[0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.nodes:
            self.nodes[key][0] = value
            self.get(key)
            return

        if len(self.nodes) >= self.capacity:
            keys = self.freqs[self.min_freq]
            evict_key = next(iter(keys))
            del keys[evict_key]
            del self.nodes[evict_key]

            if not keys:
                del self.freqs[self.min_freq]

        self.nodes[key] = [value, 1]

        if 1 not in self.freqs:
            self.freqs[1] = {}

        self.freqs[1][key] = None
        self.min_freq = 1
