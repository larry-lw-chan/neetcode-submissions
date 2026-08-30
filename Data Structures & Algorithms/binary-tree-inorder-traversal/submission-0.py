# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sorted_list = []

    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        sorted_list = []
        result = self.inorder_traverse_helper(root, sorted_list)
        if result == None:
            return []
        else:
            return result

    def inorder_traverse_helper(self, root, sorted_list):
        if not root:
            return None

        self.inorder_traverse_helper(root.left, sorted_list)
        sorted_list.append(root.val)
        self.inorder_traverse_helper(root.right, sorted_list)
        return sorted_list