class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # We can find if there is an anagram by sorting the strings alphabetically and checking if they are the same
        # s = sorted(s)
        # t = sorted(t)

        # if s == t:
        #     return True
        # return False

        # Using Hashmaps


        # Construct HashMap for letters and freq of first string
        if len(s) != len(t):
            return False

        freqS, freqT = {}, {}

        for i in range(len(s)):
            freqS[s[i]] = freqS.get(s[i], 0) + 1
            freqT[t[i]] = freqT.get(t[i], 0) + 1

        return freqS == freqT
          


        