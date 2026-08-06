class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ''' anagram is a string with the same characters as another string. Does not need to be ordered

        What my initial intuition is telling me is that I know how to directly compare two different strings and tell if they are anagrams or not. Write a function isAnagram(self, str1, str2)

        strs = ["act","pots","tops","cat","stop","hat"]

        set
        [act, cat]
        [pots. tops, stop] 
        [tops, stop]
        [cat]
        [stop]
        [hat]

        function called deconstruct
        convert a string into a dictionary containing the counts of each letter
        then can add that word to the overarching dictionary and each word that has the same key dictionary gets added to the list until the end.
        However, dictionaries are mutable and cannot be used as keys
        what if we used the sorted version of the word as the key


        strs = ["act","pots","tops","cat","stop","hat"]
        tops
        opts
        {"act": ["act"], "opts": ["pots", "opts"]}
        '''


        anagrams = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            print(sorted_s)
            if sorted_s in anagrams: 
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]

        return list(anagrams.values())
                