# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create pointer to beginning
        # Base case where the head node is the one removed
        # traverse the list until we get to the nth index node (0-indexed)
        # then find the post and 
        # two from the end
        # we can reverse the array, compute the removal, then reverse it again

        # We can also compute the length, then get the index from the start

        # Compute the length in O(n) time
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # Compute the index from the start
        n_start = length - n

        if n_start == 0:
            return head.next

        prev, curr = None, head
        for i in range(n_start):
            prev = curr
            curr = curr.next

        prev.next = curr.next

        return head

        
