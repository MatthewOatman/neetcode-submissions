from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # This is my attempt at using sorting. 

        # If we are to sort all of the values that we will have a bunch of repeating words that have the same values and then we can construct the real thing.

        temp = defaultdict(list)

        for s in strs:
            # need to sort each of the strings
            sortedS = ''.join(sorted(s))
            temp[sortedS].append(s)
        return list(temp.values())

