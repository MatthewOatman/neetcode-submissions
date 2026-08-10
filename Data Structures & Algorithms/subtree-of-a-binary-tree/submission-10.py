# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
            how do we comare if two singular node trees are subroots of eachother, 
            we can simply compare there values and if they are the same value then we can return True

            maybe as soon as we see a match in the root and the subroot values then we can go down in the dfs. 
            if they are not equal then we can return False, if they are equal then we can continue on the path down. 
        '''


        # essentially perform dfs on the root and check if the root is the same tree as the subroot each time
        if not root or not subRoot:
            return False
        stack = [root]

        while stack:
            curr = stack.pop()
            if self.same_tree(curr, subRoot):
                return True

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return False


    def same_tree(self, root1, root2):
        if not root1 and not root2:
            return True
        elif root1 and root2 and root1.val == root2.val:
            return self.same_tree(root1.left, root2.left) and self.same_tree(root1.right, root2.right)
            # The two nodes exist together but their values arent the same or one node is None while other exists
        return False
                
            
