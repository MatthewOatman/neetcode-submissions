class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        increasing order
        return [index1, index2] where first index is less than second
        O(1) additional space makes me think of pointers
        previous two sum had me dealing with sets for O(N) time and O(N) space
        sorting allows the condition for this change

        [2,4,8,9,10] and target = 13
         l        r

         if the sum of l + r < target then we move the l forward
        if the sum is larger > target we move the r right


        output would be
        [1, 4]
        '''

        l = 0
        r = len(numbers) - 1

        while l < r:
            sum = numbers[l] + numbers[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [l+1, r+1]
        



