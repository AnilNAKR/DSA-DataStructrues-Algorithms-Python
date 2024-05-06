class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
# Insertion of a new node in BST
def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue < rootNode.data:
        if rootNode.leftchild is None:
            rootNode.leftchild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftchild, nodeValue)
    else:
        if rootNode.rightchild is None:
            rootNode.rightchild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightchild, nodeValue)
    return "The node has been successfully inserted"

#Traverse a Binary Search Tree
# Pre-Order Traversal
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)

# Inorder Traversal
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftchild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightchild)

# Post Order Traversal
def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)
#Level_order Traversal
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    queue = [rootNode]
    while(len(queue)>0):
        print(queue[0].data, end = " ")
        rootNode = queue.pop(0)
        if rootNode.leftchild is not None:
            queue.append(rootNode.leftchild)
        if rootNode.rightchild is not None:
            queue.append(rootNode.rightchild)    

# Search for a value in BST
def searchNode(rootNode,nodeValue):
    if nodeValue == rootNode.data:
        return "Success -> value is found"
    elif nodeValue < rootNode.data:
        if nodeValue == rootNode.leftchild.data:
            print("Value is found")
        else:
            searchNode(rootNode.leftchild, nodeValue)
    else:
        if nodeValue == rootNode.rightchild.data:
            print("Value is found")
        else:
            searchNode(rootNode.rightchild, nodeValue)
    return "Node value not found"

# For finding the mininum value in the BST
def minValueNode(bstNode):
    current = bstNode
    while (current.leftchild is not None):
        current = current.leftchild
    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftchild = deleteNode(rootNode.leftchild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightchild = deleteNode(rootNode.rightchild, nodeValue)
    else:
        if rootNode.leftchild is None:
            temp = rootNode.rightchild
            rootNode = None
            return temp
        if rootNode.rightchild is None:
            temp = rootNode.leftchild
            rootNode = None
            return temp
        temp = minValueNode(rootNode.rightchild)
        rootNode.data = temp.data
        rootNode.rightchild = deleteNode(rootNode.rightchild, temp.data)
    return rootNode

#Delete entire BST
def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftchild = None
    rootNode.rightchild = None
    return "The BST is deleted"

newBST = BSTNode(None)
print(insertNode(newBST,70))
print(insertNode(newBST,50))
# print(newBST.data)
# print(newBST.leftchild.data)
insertNode(newBST,90)
insertNode(newBST,30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)
# preOrderTraversal(newBST)
# inOrderTraversal(newBST)
# postOrderTraversal(newBST)
# levelOrderTraversal(newBST)
# searchNode(newBST,60)
print(deleteBST(newBST))