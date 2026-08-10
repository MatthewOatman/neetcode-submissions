# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left) + 1
            right = dfs(root.right) + 1

            print("left: ", left)
            print("right: ", right, "\n")

            if abs(left - right) > 1:
                self.res = False

            return max(left, right)

        dfs(root)

        return self.res