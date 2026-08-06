# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # We can perform dfs with a counter of the depth
        return DFS_Count(root)

def DFS_Count(node):    
    # Base Case for Leaves
    if not node:
        return 0

    left_depth = 1 + DFS_Count(node.left)
    right_depth = 1 + DFS_Count(node.right)

    max_depth = max(left_depth, right_depth)
    return max_depth