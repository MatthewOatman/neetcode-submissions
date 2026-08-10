# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        '''Inverting a binary tree is essentially traversing to each node in a dfs or bfs format and swapping its left and right children and then moving to the next list'
        
        
        We can do this recursively
        '''

        if not root:
            return


        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root



        