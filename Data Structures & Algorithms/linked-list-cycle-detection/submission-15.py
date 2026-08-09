# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Cycles can be detected with the fast and slow pointer technique


        fast, slow = head, head

        # If the slow makes it to the end of the list None then no cycles
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True



        return False




        