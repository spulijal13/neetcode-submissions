# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        string = ""

        def pre(node: TreeNode):
            nonlocal string

            if not node:
                string += "N" + "%"
                return
            
            string += str(node.val) + "%"

            pre(node.left)
            pre(node.right)

            return
        
        pre(root)
        print(string)
        return string
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split('%')
        i = 0

        def buildTree():
            nonlocal i

            val = values[i]
            i += 1

            if val == 'N':
                return None
            
            node = TreeNode(int(val))

            node.left = buildTree()
            node.right = buildTree()

            return node
        return buildTree()
