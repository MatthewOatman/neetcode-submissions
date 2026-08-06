class Solution:
    def isPalindrome(self, s: str) -> bool:
        ''' Two pointer solution, one pointer at the start and one at the end
            compare the two values if they are not equal then return false. If they are simply continue.

            continuing means incrementing start pointer and decrementing end pointer. do this until the pointers cross and the start is greater than the end

            Edge cases
                even and odd lengths
                empty strings
                string of len 1
                strings with spaces ignore the spaces
        '''
        start = 0
        end = len(s) - 1

        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            elif not s[end].isalnum():
                end -= 1
                continue

            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1

        return True


