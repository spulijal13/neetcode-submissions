# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanceYourBody = True

        def calc(node: TreeNode) -> int:
            nonlocal balanceYourBody

            if not node:
                return 0
            
            left = calc(node.left)
            right = calc(node.right)

            balanceYourBody = balanceYourBody and abs(left - right) <= 1
            return 1 + max(left, right)
        
        calc(root)
        return balanceYourBody

        