# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
            Essentially what we can do is we an use dfs when we go down a level, we add 1

        what if we do the max(both the left and the right)
    
        '''
        if not root:
            return 0

        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
