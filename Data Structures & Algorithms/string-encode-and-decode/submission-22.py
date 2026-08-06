class Solution:

    '''
    So we need a way to encode a list of strings into a singular string. My first intuition is that we can just convert a list of strings into a singular string by adding each of the strings to the end of a string. 

    ex

    strs = ["Hello", "hi", "whatsup"]

    encoded = "hellohiwhatsup"

    however this makes it difficult because we have no way of knowing how to convert the encoded string into a decoded string. 
    so how can we differentiate the strings

    what if we appended the length of each of the strings to the beginning before we appended each of the strings

    "5hello2hi7whatsup"

    say we have a string thats length is greater than 10, the multiple digits make a problem because we can't simply just track the number. Thus we need a divider character between the number and the string


    10_thisismyst9_



    '''

    def encode(self, strs: List[str]) -> str:
        # Empty Edge case
        if not strs:
            return ""

        res = ""

        for s in strs:
            res += str(len(s)) + "_" + s
        
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Move j until it finds the delimiter
            while s[j] != "_":
                j += 1
            
            # Parse the complete integer length
            length = int(s[i:j])
            i = j + 1
            j = i + length
            
            # Extract the actual payload using the length
            res.append(s[i: j])
            
            # Move i past the length, delimiter, and payload string
            i = j
            
        return res





