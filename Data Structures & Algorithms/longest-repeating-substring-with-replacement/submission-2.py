class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = {}
        max_freq = 0
        res = 0

        l = 0
        for r in range(len(s)):
            sz_window = r - l + 1

            # add to the frequency
            frequencies[s[r]] = frequencies.get(s[r], 0) + 1
            max_freq = max(max_freq, frequencies[s[r]])

            # Checking our condition
            if sz_window - max_freq  <= k:
                res = max(res, sz_window)

            # Window is too large for the k replacements
            else:
                frequencies[s[l]] = frequencies[s[l]] - 1
                l += 1
        
        return res



        # when we move our left pointer, we need to decrease the frequency count by one of that value and recheck the max_freq
        # When we move our right we need to add to freq and check our max_freq