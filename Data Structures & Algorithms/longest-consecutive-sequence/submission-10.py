class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        mx = max(nums)
        mn = min(nums)
        count = 0

        st = set(nums)

        i = mn
        count = 1
        max_count = 0
        while i <= mx:
            if i in st and i + 1 in st:
                print(i)
                print(i + 1)
                count += 1
                print(count, "\n")
                i += 1 
            else:
                count = 1
                i += 1

            if count > max_count:
                max_count = count

        return max_count
        



        