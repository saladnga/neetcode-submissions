# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        queue = deque()
        res = []
        level = 0
        if root:
            queue.append(root)
        while len(queue) > 0:
            curr_level = []
            for i in range(len(queue)):
                curr = queue.popleft()
                curr_level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(curr_level)
            level += 1
        return res