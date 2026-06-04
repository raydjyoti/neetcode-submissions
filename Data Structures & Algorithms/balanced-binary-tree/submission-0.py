# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Know the depth of each node
        # Maintain an array, store max depth for each level.
        # if maxDepth - currentDepth > 1: return False

        depth = {}

        def dfs(node):

            if not node: return 0

            left = dfs(node.left)
            if left == -1: return -1

            right = dfs(node.right)
            if right == -1: return -1

            if abs(left-right) > 1: return -1

            return 1 + max(left, right)


        return dfs(root) != -1