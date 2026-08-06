#import counter from collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        rtrnArray = []
    
        for s in strs:
            tempArr = []
            #tempArr.append(s)
            #strs.remove(s)
            for s2 in strs:
                if self.findAnagrams(s, s2):
                    tempArr.append(s2)
                    #strs.remove(s2)

            if tempArr not in rtrnArray:
                rtrnArray.append(tempArr)

        return rtrnArray



    def findAnagrams(self, str1, str2) -> bool:

        if len(str1) != len(str2):
            return False
        
        count1, count2 = {}, {}

        for i in range(len(str1)):
            count1[str1[i]] = 1 + count1.get(str1[i], 0)
            count2[str2[i]] = 1 + count2.get(str2[i], 0)

        return count1 == count2