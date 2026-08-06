# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        # Essentially we need to do a bfs and swap the children all the way down until the left and the right is null
        # we can use a deque for the queue approach

        # Make a dummy node to the root
        dummy = root

        # queue for bfs
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if node == None:
                continue
            temp = node.left
            node.left = node.right
            node.right = temp

            # append the left and the right to the queue and repeat down tree
            queue.append(node.left)
            queue.append(node.right)

        return dummy


