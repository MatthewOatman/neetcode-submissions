class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]

'''
Do not need to check the conditions for the pop, top, and getMin being run on empty stacks

each function takes O(1) time

this seems easy for push, pop, top however getMin needs to be O(1) time


the first thing that I am thinking is the underlying data structure for the storing of the elements in the min stack is a list and we can simply push and pop like normal. When pushing recomputing the max is easy. We can simply compare it to the old min and if it is greater we can reassign. However with the popping we need to recalulate the min somehow. 

keeping track of the minimum needs to have 

Thinking of using a minheap. --- *** Need to read up on how heaps work in python and what the time complexity of those operations are ***

This is too slow however


In this problem we can basically make use of a prefix pattern where we have a second internal array that keeps track of the minimum value at that index



'''