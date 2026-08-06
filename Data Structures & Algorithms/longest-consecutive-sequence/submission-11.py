class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        


        '''
        We don't initially have a sorted array
        Easy brute for solution would be to sort the array in O(nlogn) time, and then count the length of the longest consecutive sequence by iterating through in 0(N) time. 


        I guess to avoid this issue and not being able to sort, what we can do is use more space to achieve the same functionality. So what I think we could do maybe utilize a set to hold the elemnts. First load them into the set in 0(n) time, then go throguh each element and use the O(1) check if the item is in a set operation and then have a counter. We can use a per item counter and then a max counter find the increasing count for each element and then assign the max counter if the current count is above the count

        Edge cases I think of: 
        - Negative numbers
        - Duplicated numbers (multiple don't count in sequence)
            - Since we can't have duplicates that shifts my mind directly to using a set
        - empty

        EX:

        [2, 20, 4, 10, 3, 4, 5]

        2, 3, 4, 5 count = 4
        max = 0 -> 4
        20 count = 1
        4, 5 count = 2
        10 count = 1
        3, 4, 5 count = 3
        4, 5 count = 2
        5 count = 1

        the numbers in the sequence to another set
        and then if we check another element where that number comes up again that was in the previous sequence then we can simply skip it. 
        '''

        # unique = [2, 20, 4, 10, 3, 5]
        # seen = {2,3,4,5}
        # count = 4
        # longest = 0

        unique = set(nums)
        seen = set()

        longest = 0
        for n in unique:
            if n in seen:
                continue
            count = 1
            seen.add(n)
            while(1):
                next = n + 1
                if next not in unique:
                    break
                count += 1
                n = next
                seen.add(next)

            if count > longest:
                longest = count
        
        return longest
            

