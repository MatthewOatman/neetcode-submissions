# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        self.flag = False

        # traversing through the root tree to get the subtrees
        def dfs(root):
            if not root:
                return

            if check_same(root, subRoot):
                self.flag = True
            
            dfs(root.left) 
            dfs(root.right)

            return


        # Essentially checking if they are the same
        def check_same(root, subroot):
            if not root and not subroot:
                return True
            if root and subroot and root.val == subroot.val:
                return check_same(root.left, subroot.left) and check_same(root.right, subroot.right)
            else:
                return False


        dfs(root)
        return self.flag