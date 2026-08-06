from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = Counter(nums)

        print(counts)

        counts_sorted = sorted(counts.keys(), key = lambda x: counts[x], reverse=True)

        print(counts_sorted)

        return counts_sorted[:k]


        