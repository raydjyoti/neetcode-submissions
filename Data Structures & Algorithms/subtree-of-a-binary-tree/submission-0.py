# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(self, s, t):
            if not s and not t: return True

            if s and not t: return False
            if not s and t: return False

            if s.val != t.val: return False

            return sameTree(self, s.left, t.left) and sameTree(self, s.right, t.right)

        if not subRoot: return True
        if not root and subRoot: return False

        if sameTree(self, root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)