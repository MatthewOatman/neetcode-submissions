# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([root]) # .append() .extend() or .popleft()
        res = []
        while queue:    
            level_vals = []
            next_level = []

            while queue:
                node = queue.popleft()
                level_vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)


            res.append(level_vals)
            queue.extend(next_level)

        return res



        