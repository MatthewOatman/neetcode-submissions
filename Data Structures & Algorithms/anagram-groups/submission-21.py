from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
    # Option 1: Sort each of the strings and make a hashmap with the key as the sorted word and a list as the collection
        hsh = defaultdict(list)
        for word in strs:
            # Make an empty list if does not exist or append the word
            # Can also use a tuple here instead of a string for faster
            sorted_word = ''.join(sorted(word))
            hsh[sorted_word].append(word)
            
        return list(hsh.values())
    
    # Option #2 



