# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.is_balanced = True

    def isBalanced(self, root: TreeNode) -> bool:
        height = self.height_finder(root)  

        # Return true if difference is less or equal to 1
        return self.is_balanced

    def height_finder(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        # Do Math
        left_height = self.height_finder(root.left)
        right_height = self.height_finder(root.right)
        # print(f"left: {left_height} right: {right_height}")

        if abs(left_height - right_height) > 1:
            self.is_balanced = False

        return 1 + max(left_height, right_height)