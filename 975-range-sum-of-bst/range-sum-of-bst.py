# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def bounds(val):
            if val<=high and val>=low:
                return True
            return False
        def dfs(root):
            if root is None:
                return 0
            leftval=dfs(root.left)
            rightval=dfs(root.right)
            if bounds(root.val):
                return root.val+leftval+rightval
            return leftval+rightval
        return dfs(root)
        