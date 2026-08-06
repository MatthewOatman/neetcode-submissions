class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        
        # 1. Turn the list into a min-heap (modifies in-place)
        heapq.heapify(self.heap)
        
        # 2. Pop the smallest elements until we only have the k largest left
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # 1. Add the new value to the heap
        heapq.heappush(self.heap, val)
        
        # 2. If adding this value pushes our heap size past k, pop the smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # 3. The smallest element in a heap of size k is the kth largest overall
        return self.heap[0]