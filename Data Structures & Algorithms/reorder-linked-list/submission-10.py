# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Use a fast and slow pointer technique to find the middle of the list


        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        right_half = slow.next
        slow.next = None

        prev, curr = None, right_half

        # Reverse the order of the second half
        while curr:
            post = curr.next 
            curr.next = prev
            prev = curr
            curr = post

        # zip the two halves together
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
