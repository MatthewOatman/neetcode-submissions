# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # edge case #1 is that a node can be a descendant of itself


        # so the lowest ancestor always has to be between or equal the two numbers

        stack = [root]
        pv = p.val
        qv = q.val

        while stack:
            node = stack.pop()
            if node.val > qv and node.val > pv:
                stack.append(node.left)
            elif node.val < qv and node.val < pv:
                stack.append(node.right)
            else:
                return node
        




        