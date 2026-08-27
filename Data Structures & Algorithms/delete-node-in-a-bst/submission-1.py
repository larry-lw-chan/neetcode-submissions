# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        root = self.remove(root, key)
        return root

    def remove(self, root: TreeNode | None, key: int) -> TreeNode | None:
        # Base Case
        if not root:
            return None

        if key < root.val:
            root.left = self.remove(root.left, key)
        elif key > root.val:
            root.right = self.remove(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else:
                min_node = self.find_min(root.right)
                root.val = min_node.val
                root.right = self.remove(root.right, min_node.val)

        return root

    def find_min(self, root: TreeNode | None):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def search_node(self, root: TreeNode | None, key: int) -> TreeNode | None:
        # Base Case - None Found
        if not root:
            return None