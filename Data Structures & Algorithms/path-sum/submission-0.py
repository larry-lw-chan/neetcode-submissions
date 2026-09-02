# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.found = False
        self.tracker = 0

    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        self.pathsum_helper(root, targetSum)
        return self.found

    def pathsum_helper(self, root: TreeNode | None, targetsum: int) -> TreeNode | None:
        if not root:
            return None

        # Add root value to tracker
        self.tracker += root.val

        # Check if found
        if root.left == None and root.right == None and self.tracker == targetsum:
            self.found = True

        # Traverse
        self.pathsum_helper(root.left, targetsum)
        self.pathsum_helper(root.right, targetsum)

        # Remove value from tracker
        self.tracker -= root.val

        return root
        