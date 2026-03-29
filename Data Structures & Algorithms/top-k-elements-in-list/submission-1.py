class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0) + 1

        bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in counter.items():
            bucket[freq].append(num)

        result = []

        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result