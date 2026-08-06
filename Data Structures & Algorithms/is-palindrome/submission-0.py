class Solution:
    def isPalindrome(self, s: str) -> bool:
        # we can use a two pointer solution
        left, right = 0, len(s) - 1

        s = s.lower()

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while right > left and not s[right].isalnum():
                right -= 1
            # check if the values are not equal
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1

        return True