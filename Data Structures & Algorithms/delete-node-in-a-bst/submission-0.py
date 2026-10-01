# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Time complexity: O(logn)
        # Space complexity: O(h)

        def min_node(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr

        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # 2 children, replace with the smallest right value
            successor = min_node(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        return root