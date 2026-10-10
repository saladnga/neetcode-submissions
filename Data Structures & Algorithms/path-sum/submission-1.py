# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Time Complexity: O(N)
        # Space Complexity: O(H) - height tree

        def backtrack(node, curr):
            if not node:
                return False
            curr += node.val
            # Ensure leaf node and equal to targetSum
            if not node.left and not node.right and curr == targetSum:
                return True
            return backtrack(node.left, curr) or backtrack(node.right, curr)

        return backtrack(root, 0)
        
