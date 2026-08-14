# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ''' A valid BST is valid if every node's left is smaller and every nodes right is larger. 

    We can simulate this in O(n) time by simply traversing to every element in a BFS or DFS pattern and then checking if the left node is less than the right.
        '''
        
        
        #          0
        #     -1000  1000
        #   null null 0

        # This solution does not work with the above example because 0 is not strictly greater than the root 0. we need to define an interval that grows or shrinks depending on the size of the binary tree we will start the interval in each of the nodes and then subtract every time we go down a side of the tree if we get to a node that does not fit within the constraints of the window then we immediately return false

        def dfs(root, window):
            if not root:
                return True

            if not (window[0] < root.val < window[1]):
                return False

            left = dfs(root.left, [window[0], root.val])
            right = dfs(root.right, [root.val, window[1]])

            return left and right


        window = [float('-inf'), float('inf')]
        res = dfs(root, window)
        return res











        

        valid = True

        if not root:
            return True

        if root.left and root.left.val >= root.val:
            valid = False
        elif root.right and root.right.val <= root.val:
            valid = False

        if valid == False:
            return False

        left = self.isValidBST(root.left) 
        right = self.isValidBST(root.right)

        return True

    

