# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
            how do we determine if a node has no larger value betwen the root and itself. We can iterate down the tree and hold a maximum value we have seen on the way down we can pass a max through one of the parameters in dfs and then have a global variable count that we increment if the value is greater than the max at that level 
        '''

        count = 0
        max_seen = float('-inf')

        def dfs(root, max_seen):
            nonlocal count

            if not root:
                return

            if root.val >= max_seen:
                max_seen = root.val
                count += 1

            

            dfs(root.left, max_seen)
            dfs(root.right, max_seen)


        dfs(root, max_seen)
        return count





        
        