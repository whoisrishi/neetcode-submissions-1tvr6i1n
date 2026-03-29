class MyHashSet:
    def __init__(self):
        self.bucket_count = 1000
        self.buckets = [[] for _ in range(self.bucket_count)]

    def _hash(self, key: int) -> int:
        return key % self.bucket_count

    def _get_bucket(self, key: int):
        bucket_index = self._hash(key)
        return self.buckets[bucket_index]

    def add(self, key: int) -> None:
        bucket = self._get_bucket(key)
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self._get_bucket(key)
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket = self._get_bucket(key)
        return key in bucket