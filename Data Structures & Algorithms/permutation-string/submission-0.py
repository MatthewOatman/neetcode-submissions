class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        '''
        Notes

        substring can be identified using a has map or 26 len array of that string


        what we can do is create a list of 26 len all starting at 0. Create a sliding window the size of the length of s1. If a character is included in the window we ad that to a new hashmap and if the right pointer gets incremented if the string is not found then the value at the right pointer gets added to the list, if the left pointer moves then we decrement the index associated with that value
        ord(char) - ord(a)


        s1 = "ab"

        s2 = "lecaabee"

        s1_map = [1,1,1,0,0,0,0,0,....]

        '''


        s1_hash = [0] * 26
        s2_hash = [0] * 26

        # construct the hash array for s1
        for c in s1:
            s1_hash[ord(c)-ord('a')] += 1


        l = 0
        for r in range(len(s2)):
            s2_hash[ord(s2[r])-ord('a')] += 1

            # If a matching subset is found
            if s2_hash == s1_hash:
                return True

            # Moving left pointer if the window is of size
            if (r - l + 1) == len(s1):
                # then we have to remove that from the s2_hash
                s2_hash[ord(s2[l])-ord('a')] -= 1
                l += 1
                
                


        return False



