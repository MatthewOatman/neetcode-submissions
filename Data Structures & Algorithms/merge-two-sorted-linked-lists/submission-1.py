# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        '''
        Essentially we need to loop through both the list1 and list2 at the same time

        we compare the current elements values and add the smaller one to the front of the linked list we are constructing.

        to construct one we can use a dummy and then a current node which starts as dummy.next whichever linked list has the smaller element from it we can move to the next item within that linked list
        '''
        curr = dummy = ListNode(0)
        # oh this is because dummy.next is still 0

        # Loop list1 and list2 will serve as pointers to their current element
        while list1 or list2:
            # checking to see if list1 or list2 is already at the end
            if list1 and not list2:
                curr.next = list1
                list1 = list1.next
            elif list2 and not list1:
                curr.next = list2
                list2 = list2.next
            else:
                # Both have values
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    print(curr.val)
                    list2 = list2.next

            curr = curr.next

        return dummy.next





            
        