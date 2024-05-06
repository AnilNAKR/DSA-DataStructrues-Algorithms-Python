class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def preOrderTraversal(root):    
    if root:
        print(root.value, end=" ")
        preOrderTraversal(root.left)
        preOrderTraversal(root.right)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(8)
root.right.right = TreeNode(9)
preOrderTraversal(root)