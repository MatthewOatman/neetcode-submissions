# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:

        if not pairs:
            return []
        res = []
        res.append(pairs[:])
        # Start with the second item assuming that the first is sorted
        for i in range(1, len(pairs)):
            val = pairs[i].key

            j = i - 1
            while j >= 0 and val < pairs[j].key:
                # Perfrom the swap
                pairs[j+1], pairs[j] = pairs[j], pairs[j+1]
                j -= 1

            res.append(pairs[:])

        return res


        # 1 5 | _0_ 6 8 13 4 





