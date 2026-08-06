class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        '''
        army
        ramy

        d1 = {a: 1, r: 1, m: 1, y: 1}
        d2 = {a: 1, r: 1, m: 1, y: 1}
        '''
        # S loop
        d1 = dict()
        for c in s:
            d1[c] = d1.get(c, 0) + 1
        

        # T loop
        d2 = dict()
        for c in t:
            d2[c] = d2.get(c, 0) + 1

        if d1 == d2: 
            return True

        return False