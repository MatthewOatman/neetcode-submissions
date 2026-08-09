"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        '''
        The constraints have 0 <= n <= 100. Meaning a brute force solution is potentially fine thus can probably get away with a O(n^2) or even O(n^3) solution at the slowest. 

        One thing that I am wondering is are cycles allowed? The normal links I think cannot but the random links can be


        head = [[3,null],[7,3],[4,0],[5,1]]

        How would we create a copy for a normal linked list

        We would have a curr that points to the head
        then create a new node with that same value and set that to prev, then do do new = new.next and curr = curr.next


        dummy = Node(0)
        curr = dummy

        for value in values:
            curr.next = Node(value)
            curr = curr.next

        new_list = dummy.next

        maybe we can store a reference to that node in the random


        So since when iterating through the list we can't immediately assign a nodes random pointer because the object that it points to might not be initialized yet. Thus we can create the copies of all the nodes in the linked list and then go back assigning the random pointers. However in order to do this we need to store the addresses of the copies


    [1, 2, 3]

    we created
    [1, 2, 3]

    then go through again see 1 points random to null, we can assign this
    then go to 2 and see it points to 3

    oh so we have a hashmap that stores the original node: new node
        '''
        old_to_new = {}
        old_to_new[None] = None

        # Step 1: Go through making deep copied list without random pointers

        dummy = Node(0)
        curr = dummy

        old_node = head
        while old_node:
            value = old_node.val
            new_node = Node(value)

            old_to_new[old_node] = new_node

            curr.next = new_node

            old_node = old_node.next
            curr = curr.next

        # Step 2: Go through the head and dummy again and assing the new randoms

        curr = dummy.next
        while head:
            random_node = head.random

            new_random = old_to_new[random_node]
            curr.random = new_random

            curr = curr.next
            head = head.next

        return dummy.next


        