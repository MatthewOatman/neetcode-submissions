# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Dummy pointer to the head of the smallest list
        # Node is used to help create LL
        dummy = node = ListNode()

        # Iterate through both of the lists until end of one of the lists
        while list1 and list2:
            # Compare the values
            v1 = list1.val
            v2 = list2.val

            # Assign v1 as next smallest
            if v1 < v2:
                node.next = list1
                list1 = list1.next

            # Assign v2 as next smallest
            elif v2 <= v1:
                node.next = list2
                list2 = list2.next

            node = node.next
            
        #append the remaining nodes to node list
        node.next = list1 or list2

        return dummy.next




