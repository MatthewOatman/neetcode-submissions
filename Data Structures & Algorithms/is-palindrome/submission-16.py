class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Define the left and the right pointer
        l, r = 0, len(s) - 1

        while l < r:
            # Need the while loop condition because if all non alnum characters then the pointers can exceed each 
            # other and cause index out of bounds errors
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            # Compare the strings
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

            
        

        