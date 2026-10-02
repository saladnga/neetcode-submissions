# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)

        # def get_height(root):
        #     if not root:
        #         return 0
        #     left = get_height(root.left)
        #     right = get_height(root.right)
        #     return 1 + max(left, right)
        
        # if not root:
        #     return True
        # left_subtree = get_height(root.left)
        # right_subtree = get_height(root.right)
        # if abs(left_subtree - right_subtree) <= 1:
        #     return True
        # return False

        # Time Complexity: O(n)
        # Space Complexity: O(n)
        if not root:
            return True
        def dfs(root):
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]