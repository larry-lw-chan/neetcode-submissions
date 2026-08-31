
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # Edge Case
        if not preorder or not inorder:
            return None
        mapping = {val: i for i, val in enumerate(inorder)}
        
        def build_helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None
            
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            mid = mapping[root_val]
            left_size = mid - in_start
            
            root.left = build_helper(pre_start + 1, pre_start + left_size, in_start, mid - 1)
            root.right = build_helper(pre_start + left_size + 1, pre_end, mid + 1, in_end)
            return root
            
        return build_helper(0, len(preorder) - 1, 0, len(inorder) - 1)