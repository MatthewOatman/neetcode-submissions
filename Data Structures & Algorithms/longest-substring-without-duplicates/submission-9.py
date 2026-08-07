class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            Mind immediately goes to double pointer beacause we need to iterate throught the string finding the max length


            returning the number



            "zxyzxyz"
            l = 0
            r = 0

            while r < len(s):
            1. start with a default length of max substring as 1
            2. initialize the l and r as 0 and create an empty set
            3. Have a while loop that is while r < len(s)
            4. check if the current character at r is in the set
            5. If the character is in the set then we move the l to the r
            2. check if the characters are different, if so then we increment the counter and increment r += 1
            3. if the characters are the same then we move the left pointer += 1
            4. every time we move the right pointer we are incrementing the counter.

        '''
        # Base Case
        if len(s) == 0:
            return 0

        l, r = 0, 0
        length = 0
        max_length = 0
        seen = set()

        while r < len(s):
            length += 1
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                length -= 1
            
            seen.add(s[r])
            r += 1

            max_length = max(max_length, length)

        return max_length
                



