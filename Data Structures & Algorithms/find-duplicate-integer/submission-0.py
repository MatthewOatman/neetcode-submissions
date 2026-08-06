class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(N) space with O(N) time complextity

        seen = set()

        for n in nums:
            if n in seen:
                return n
            else:
                seen.add(n)
        
        