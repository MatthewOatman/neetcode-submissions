# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        INPUT:   1 -> 2 -> 3 -> 4 -> 5 -> 6

        GOAL:    1 -> 6 -> 2 -> 5 -> 3 -> 4

        Step 1 (Split):    [1 -> 2 -> 3]   and   [4 -> 5 -> 6]
        Step 2 (Reverse):  [1 -> 2 -> 3]   and   [6 -> 5 -> 4]
        Step 3 (Merge):    1 -> 6 -> 2 -> 5 -> 3 -> 4

        edge cases
        size 1 [1]
        size 2 [1 -> 2]

        English pseudo code (breaking it up into smaller problems):
        # 1. Find middle of list (Fast & Slow pointers)
        # 2. Reverse the second half of the list
        # 3. Interleave/Merge two lists back together   

        "Before I start typing code, let me trace a concrete example. I see     that $N$ is up to 1,000, so a naive $O(N^2)$ search for the tail in a loop won't pass. I need an $O(N)$ approach. Looking at the desired output, it looks like interleaving the first half with the reversed second half. Let me sketch out those 3 sub-steps first to make sure my pointer manipulation is clean."

        '''
        # Edge case for length 1
        # if not head.next:
        #     return head

        # Step 1: Split the array in half 
        # Starting fast at .next ensures always finds end of first half
        fast, slow = head.next, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next  # 1. Store the start of the second half
        slow.next = None    # 2. Chop off the first half

        
        # Step 2: Reverse the second half
        
        curr = second
        prev = None
        while curr:
            post = curr.next
            curr.next = prev
            prev = curr
            curr = post

        second = prev

        node = dummy = ListNode(0)


        # Step 3: Merge the arrays:
        while head and second:
            node.next = head
            head = head.next

            node.next.next = second
            second = second.next

            node = node.next.next


        # Adding the remaining to the end
        node.next = head or second




        

        