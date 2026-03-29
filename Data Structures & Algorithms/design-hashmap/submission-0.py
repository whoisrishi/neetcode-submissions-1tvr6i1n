class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.data = [[] for _ in range(self.size)]

    def _get_hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hash_index = self._get_hash(key)
        inner_list = self.data[hash_index]

        for i, item in enumerate(inner_list):
            if item[0] == key:
                inner_list[i] = (key, value)
                return

        inner_list.append((key, value)) 

    def get(self, key: int) -> int:
        hash_index = self._get_hash(key)
        inner_list = self.data[hash_index]

        for k, v in inner_list:
            if k == key:
                return v

        return -1

    def remove(self, key: int) -> None:
        hash_index = self._get_hash(key)
        inner_list = self.data[hash_index]

        for i, (k, v) in enumerate(inner_list):
            if k == key:
                inner_list.pop(i)
                return