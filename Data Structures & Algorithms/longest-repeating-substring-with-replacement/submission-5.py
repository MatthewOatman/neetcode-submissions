class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''

        AAAABBAABAABA k = 2

        8 characters long As

        ABABABABBAA k = 3

        7 characters long Bs

        So we need an algorithm that would check each type of the strings.

        Moreover, strings can have more than one type of letter


        ABABBAA k = 1
           ---
        maybe we have a store of each character and their frequencies in the current substring
        look for character with keys in hashmap that arent s[l] and reduce count of k available

         do we have to compare the value to s[l]?

        res = 4


 we move left pointer if we find len window (r - l + 1) - max freq > k

        '''

        l = 0

        freq = {}
        max_length = 0
        max_freq = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            # need to get the max frequency
            max_freq = max(freq.values())
            while r - l + 1 - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        
        return max_length

            





