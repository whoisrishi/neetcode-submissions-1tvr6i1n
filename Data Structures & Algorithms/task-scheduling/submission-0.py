class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = [0] * 26

        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        max_freq = max(freq)

        max_count = 0
        for f in freq:
            if f == max_freq:
                max_count += 1

        return max((max_freq - 1) * (n + 1) + max_count, len(tasks))