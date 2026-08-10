# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ''' 
        DFS with both at the same time?? and comparing

        '''
        self.same = True

        def dfs(root1, root2):
            if root1 and root2 and root1.val != root2.val:
                self.same = False
                return 
            elif root1 and not root2:
                self.same = False
                return
            elif root2 and not root1:
                self.same = False
                return
            elif not root1 and not root2:
                return

            dfs(root1.left, root2.left)
            dfs(root1.right, root2.right)

            return
        
        dfs(p, q)
        return self.same

            

            
