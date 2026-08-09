# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ''' 
        I am going to explain to you how I interpret the problem to wake sure I am focused on the correc things.

        First we are given a linked list of size1 to 30 and are given an int n which represents the nth node from the end of the list that being (1-indexed) and then return the head of the list.

        This linked list contains all only integers


        input = [5, 4, 3, 2, 1] n = 3

        output = [5, 3, 2, 1]

        Since the nodes are pointing down the list and not back we cannot simply go backwards so we are going to need a singular foward pass solution

        Looking at the sz constraints it seems to me that we are looking for a O(n) time solution with O(1) space

        Solution 1:

            1. Reverse the array O(n)
            2. Remove the element n (1-indexed) from start O(n)
            3. Reverse it again O(n)

        This however takes unnecessary compute time is there a way to do it with one singular pass?


        Solution 2: Two pointer technique

        Since n has to be within size constraints we can seperate the two pointers by the distance of the n. when the fast pointer reaches the end then we know that we are at the element that we need to remove

        [5, 4, 3, 2, 1],  n = 3

        left = 5
        right = 2 (three nexts)

        let n = 3


        Examples

        [2, None] n = 2

        left = 2
        right = None
        temp = None

        Incorrect, so I am having an issue where if the n is the length of the array it is working improperly. How about setting curr to dummy?

        [1] n = 1

        left = dummy
        right = 1
        temp = 1

        '''
        if not head.next:
            return None

        dummy = ListNode(0,head)

        curr = dummy

        left = curr
        right = curr
        for i in range(n):
            right = right.next

        while right and right.next:
            right = right.next
            left = left.next

        temp = left.next.next
        left.next = temp

        return dummy.next