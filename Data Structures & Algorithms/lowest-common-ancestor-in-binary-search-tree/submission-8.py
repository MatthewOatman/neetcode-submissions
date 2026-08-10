# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

#         '''
#         Notes:
#         - all values are unique
#         - Key is binary search tree so ordered
#         - LCA = the lowest node root that is shared between both of the nodes such that they are both decendants
#             - Can think of this as the grandparent

#         The ancestor is allowed to be a decendany of itself. Thus the lowest common ancestor in a default condition would simply be itself.

#         so we can think of this is that if they are comprised of the same tree where one of the nodes is the root, then both of their LCA is simply that root.

#         - p != q
#         - p and q both exists in the BST


#         Brainstorming:
#             Obviously we are going to implement some type of dfs or bfs solution. 

#         so if we go down a subtree and then the root we see is p or q then we know that that is 



#         what if we go through every root in a dfs or bfs fashion and for each of the roots we check if the p and q is found within the subtree. we can do this by using two return values one bool for p and one bool for q. 

#         if at the end they are both true, then we return the current root
#         '''
#         res = root
#         self.p_found = False
#         self.q_found = False
#         queue = deque()
#         queue.append(root)

#         while queue:
#             curr = queue.popleft()
#             if curr.left:
#                 queue.append(curr.left)
#             if curr.right:
#                 queue.append(curr.right)

#             self.nodesInTree(curr, p, q)

#             if self.p_found and self.q_found:
#                 res = curr

#             self.p_found = False
#             self.q_found = False

#         return res


#     def nodesInTree(self, root, p, q):
#         if not root:
#             return
#         if root.val == p.val:
#             self.p_found = True
#         if root.val == q.val:
#             self.q_found = True
#         self.nodesInTree(root.left, p, q)
#         self.nodesInTree(root.right, p, q)


# """
# This solution is a little non-optomized

# the average runtime complexity is O(n*logn)
# the space complexity is O(nlogn) for the call stack and the queue I think 


        '''Bottom up approach is a better way of doing it'''

        # if not root or root == p or root == q: 
        #     return root

        # # Search left and right subtrees
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if left and right:
        #     return root

        # return left if left else right


        """ Binary search tree iteration solution"""


        curr = root

        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else:
                return curr










        