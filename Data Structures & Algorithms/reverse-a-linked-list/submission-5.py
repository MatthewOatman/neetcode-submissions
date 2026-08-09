# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        '''
        Say that we have a linked list liked this

        1 -> 2 -> 3 -> 4 -> 5 -> None

        start down here at 1
        
        curr = None

        get 1's next as temp

        assign 1.next = curr

        curr = 1

        loop over again 

        assign temp.next 

        5 -> 4 -> 3 -> 2 -> 1 -> None

        To reverse a linked list we need to create a dummy node and assign its next to the head. 

        we may be able to do this with a stack

        while curr:
            curr = head to start


        The brute force that uses more space complexity is using a stack and then appending the the values to it as we traverse to the end of the array and then popping and then creating the linked list

        '''
        # 3 -> 2 -> 1 -> None
        # prev = 3
        # curr = None
        # post = None
        
        prev = None
        curr = head

        while curr != None:
            post = curr.next
            curr.next = prev
            prev = curr
            curr = post

        return prev
        