# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxH = 0

        def dfs(node, h):
            if not node: return

            self.maxH = max(self.maxH, h)
            dfs(node.left, h+1)
            dfs(node.right, h+1)

        dfs(root, 1)

        return self.maxH
