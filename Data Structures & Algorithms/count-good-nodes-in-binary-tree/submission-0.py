# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def maxNodes(root: TreeNode, max_val: int) -> int:
            if not root:
                return 0
            
            count = 0
            
            if max_val is None or root.val >= max_val:
                count += 1
                curr_max = root.val
            else:
                curr_max = max(root.val, max_val)
            
            count += maxNodes(root.right, curr_max) + maxNodes(root.left, curr_max)

            return count
    
        return maxNodes(root, None)