# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Cycle in a linked list can be found by setting a boolean to revisited or finding a loop through the repeated visit
        # Maybe we can change the value to something special to determine if it has been visited or not

        # what if I create a set of visited

        # visited = set()

        # curr = head
        # while curr:
        #     # Found a cycle
        #     if curr in visited:
        #         return True
        #     # add to the visited set
        #     visited.add(curr)
        #     # Iterate through the linked list
        #     curr = curr.next
        
        # return False


        # Fast and slow pointer solution
        # O(N) time complexity, O(1) space complexity


        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False