# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        return self.solve(root)
    def solve(self,root,depth = 0):
        if root == None:
            return depth
        return max(self.solve(root.left,depth+1),self.solve(root.right,depth+1))

        """
        :type root: TreeNode
        :rtype: int
        """
        
