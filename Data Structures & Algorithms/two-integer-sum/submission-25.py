class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # first initial solution in my head is to have a double for loop checking all possible combinations in O(n^2) time complexity


        # Another is to have two pointers, (assuming that the nums array is sorted) we can have one pointer at the start of the array
        # and one at the end of the array. we can compute the sum and then if the sum < goal we can increment the left pointer and if 
        # too large can decrement the right pointer
        # Important to note that we cannot assume the ascending order approach so we must sort the array

        # A = []
        # # Create a new array where we store the original indexes
        # for i, num in enumerate(nums):
        #     A.append((i, num))

        # # sort by the num value not the default index using a lambda expression
        # A.sort(key=lambda x: x[1])

        # # Initialize the pointers
        # left = 0
        # right = len(nums) - 1

        # # iterate through the array
        # while left < right:
        #     current_sum = A[left][1] + A[right][1]
        #     if current_sum == target:
        #         # Since the order is rearranged by sorting have to put back
        #         return [min(A[left][0], A[right][0]),
        #                 max(A[left][0], A[right][0])]
        #     elif current_sum < target:
        #         left += 1
        #     else:
        #         right -= 1

        # return []


        # Third approach is to use a hashmap or dict where the key is the number and the val is the index

        d = {}
        for i, n in enumerate(nums): 
            rem = target - n
            if rem in d:
                return [min(d[rem], i),
                        max(d[rem], i)]
            d[n] = i
        return []
