# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return depth

"""
答案：简单直接
"""