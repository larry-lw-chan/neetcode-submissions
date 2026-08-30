# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.counter = 0
        self.result = None

    def kthSmallest(self, root: TreeNode | None, target: int) -> int | None:
        self.inorder_traverse(root, target)
        return self.result

    def inorder_traverse(self, root, target):
        if not root:
            return None

        self.inorder_traverse(root.left, target)

        # Do Math and Algo
        self.counter += 1
        if self.counter == target:
            self.result = root.val

        self.inorder_traverse(root.right, target)

        return None
        