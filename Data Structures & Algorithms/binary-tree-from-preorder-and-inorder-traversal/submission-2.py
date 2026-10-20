# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {}

        for i, val in enumerate(inorder):
            index_map[val] = i
        
        pre_index = 0

        def build(left: int, right: int):
            nonlocal pre_index

            if left > right:
                return None
            
            root = TreeNode(preorder[pre_index])
            pre_index += 1

            i = index_map[root.val]

            root.left = build(left, i - 1)
            root.right = build(i + 1, right)

            return root
        return build(0, len(inorder) - 1)



        

        
