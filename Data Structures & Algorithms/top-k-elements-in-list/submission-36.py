class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        nums = [3,1,2,3,3,2], k = 2
                val: count
        freq = {3: 3, 2: 2, 1: 1}


        '''

        freq = {}
        # Building the freq dict
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        count_to_num = {}
        
        # building the opposite array
        for n, count in freq.items():
            if count in count_to_num:
                count_to_num[count].append(n)
            else:
                count_to_num[count] = [n]

        
        sorted_keys = sorted(count_to_num, reverse=True)

        res = []
        for key in sorted_keys:
            res.extend(count_to_num[key])

        return res[:k]



        

