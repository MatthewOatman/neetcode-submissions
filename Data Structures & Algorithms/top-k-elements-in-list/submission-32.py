from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


    # If I understand the problem correctly say that I had an array like this
    # [a, a, a, b, b, b, b, c, c, d, e, e, e, e, f] and k = 3 I would return a, b, e. What happens in the case of a tie? 

    # Attempt #1: Create a hashmap where the word is the key and the frequency is the value. Iterate through the nums and increment
    # This would come into issues where I would get the values and then I couldn't get the keys from the values. Thus I need to have it where the keys are the frequency

        # hsh = defaultdict(list)
        # for n in nums:
        #     freq = nums.count(n)
        #     hsh[freq].append(n)


        # print((nums.count))
        # # print(sorted(hsh.items()))

    # Option #1: Sorting (count freq, sort by freq, take the top k)
        # # Get Freq
        # count = {}
        # for n in nums: 
        #     count[n] = count.get(n, 0) + 1

        # # Sort
        # arr = []
        # for n, cnt in count.items():
        #     arr.append((cnt, n))
        # arr.sort(reverse=True)

        # # Pick the k most frequent
        # fin = [t[1] for t in arr[0:k]]
        # return fin

    # Option #2:I could also have an array with len2000 and then have a frequency array
    # Max frequency is n

    # Option #3: Using a min-heap - this marginally reduces the runtime and increases the space complexity

    # Option #4: Using bucket sort - max possible frequency is the number of elements in the array. Thus can create a list where the frequency is the index in the array and we store all the numbers that appear exactly once

        # Create the buckets
        buckets = [[] for i in range(len(nums) + 1)] # 0 - N

        # Build the frequency map
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # Added the numbers to the buckets
        for num, cnt in count.items():
            buckets[cnt].append(num)


        # Find the top K 
        flat = [item for b in buckets for item in b]

        return flat[-k:]
        




    # Option #5: using the counter collection as more simple version of option 1
        # hsh = defaultdict(list)
        # counter = collections.Counter(nums)
        # common = counter.most_common(k)
        # return list(dict(common).keys())