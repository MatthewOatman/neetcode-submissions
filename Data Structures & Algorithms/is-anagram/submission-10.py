class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # An anagram is defined as having two words built of the same letters
        # We can find if they are anagrams by creating a hash set and

        s = sorted(s)
        t = sorted(t)

        print(s)
        print(t)

        if s == t:
            return True

        return False