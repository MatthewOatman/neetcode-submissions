class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        '''
        Notes:
        we can use the sliding window technique to create at least a substring of len(t) needs to be found within s to find all the elements in t
        
        can create the frequency array of t and maybe can create another one that is a copy and whenever we see an element from the first string we decrement that index for that character. At the end we wil check if not any(freq)


    Rules for expanding or closing window:
    
    we always expand the right pointer. 
    Left pointer expansion: 

    so maybe once we get our first answer we store it and then fater we get that answer we move the left over until it reaches another character in t again then we continue moving right
        '''

        if not s or not t or len(s) < len(t):
            return ""

        target_counts = Counter(t)
        window_counts = {}

        # 'required' is unique chars in t; 'formed' tracks how many unique chars hit target count
        required = len(target_counts)
        formed = 0

        l = 0
        best_len = float("inf")
        best_window = (0, 0)

        for r in range(len(s)):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            # If current char count matches target count in t
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            # Shrink window from the left as long as it remains valid
            while l <= r and formed == required:
                # Save the smallest valid window so far
                if (r - l + 1) < best_len:
                    best_len = r - l + 1
                    best_window = (l, r)

                # Remove left character to shrink window
                left_char = s[l]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    formed -= 1
                l += 1

        start, end = best_window
        return s[start:end + 1] if best_len != float("inf") else ""
        







    