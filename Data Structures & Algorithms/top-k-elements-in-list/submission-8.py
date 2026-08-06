from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


    # If I understand the problem correctly say that I had an array like this
    # [a, a, a, b, b, b, b, c, c, d, e, e, e, e, f] and k = 3 I would return a, b, e. What happens in the case of a tie? 

    # Option #1: Create a hashmap where the word is the key and the frequency is the value. Iterate through the nums and increment
    # This would come into issues where I would get the values and then I couldn't get the keys from the values. Thus I need to have it where the keys are the frequency

        hsh = defaultdict(list)
        counter = collections.Counter(nums)
        common = counter.most_common(k)
        return list(dict(common).keys())


    # I could also have an array with len2000 and then have a frequency array

