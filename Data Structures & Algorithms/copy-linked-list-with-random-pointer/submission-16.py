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
        
        # copy the nodes normally and to copy the random
        # when creating the nodes we can traverse from start to end however with random some point to nodes we have not yet created yet

        # first pass we just create copies of the new nodes and we create a hashmap were we assign old nodes to new
        # on second pass we find next and use mapping in hashmap and random and use mapping in hashmap to assign

        oldToNew = {None:None}

        # Creating the dictionary and the nodes
        curr = head
        while curr:
            new = Node(curr.val)
            oldToNew[curr] = new
            curr = curr.next

        curr = head
        while curr:
            copy = oldToNew[curr]
            copy.next = oldToNew[curr.next]
            copy.random = oldToNew[curr.random]
            curr = curr.next
        
        return oldToNew[head]




        