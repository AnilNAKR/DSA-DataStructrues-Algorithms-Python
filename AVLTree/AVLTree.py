class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1
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

#insertion of a node in an AVL Tree
# important - Checking height of the rootnode -> Helper Function
def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

# right Rotation
def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftchild
    disbalancedNode.leftchild = disbalancedNode.leftchild.rightchild
    newRoot.rightchild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftchild),getHeight(disbalancedNode.rightchild))
    newRoot.height = 1 + max(getHeight(disbalancedNode.leftchild),getHeight(disbalancedNode.rightchild))
    return newRoot

# Left Rotation
def leftRotation(disbalancedNode):
    newRoot = disbalancedNode.rightchild
    disbalancedNode.rightchild = disbalancedNode.rightchild.leftchild
    newRoot.leftchild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftchild),getHeight(disbalancedNode.rightchild))
    return newRoot

# get the balance of the root node
def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftchild) - getHeight(rootNode.rightchild)

def insetNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue <= rootNode.data:
        rootNode.leftchild = insetNode(rootNode.leftchild, nodeValue)
    else:
        rootNode.rightchild = insetNode(rootNode.rightchild, nodeValue)

    rootNode.height = 1 + max(getHeight(rootNode.leftchild), getHeight(rootNode.rightchild))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftchild.data:
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.leftchild.data:
        rootNode.leftchild = leftRotation(rootNode.leftchild)
        return leftRotation(nodeValue)
    if balance < -1 and nodeValue > rootNode.rightchild.data:
        return leftRotation(rootNode)
    if balance < -1 and nodeValue < rootNode.rightchild.data:
        rootNode.rightchild = rightRotate(rootNode.rightchild)
        return leftRotation(rootNode)
    return rootNode

def getMinValue(rootNode):
    if rootNode is None:
        return rootNode
    return getMinValue(rootNode.leftchild)

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftchild = deleteNode(rootNode.leftchild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightchild = deleteNode(rootNode.rightchild, nodeValue)
    else:
        if rootNode.leftchild is None:
            temp = rootNode.rightchild
            rootNode = None
            return temp
        elif rootNode.rightchild is None:
            temp = rootNode.leftchild
            rootNode = None
            return temp
        temp = getMinValue(rootNode.rightchild)
        rootNode.data = temp.data
        rootNode.rightchild = deleteNode(rootNode.rightchild, temp.data)
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftchild) >= 0:
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightchild) <= 0:
        return leftRotation(rootNode)
    if balance > 1 and getBalance(rootNode.leftchild) < 0:
        rootNode.leftchild = leftRotation(rootNode.leftchild)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightchild) > 0:
        rootNode.rightchild = rightRotate(rootNode.rightchild)
        return leftRotation(rootNode)
    
    return rootNode

#Delete entire AVL Tree
def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftchild = None
    rootNode.rightchild = None
    return "The AVL Tree has been successfully deleted"



newAVL = AVLNode(5)
newAVL = insetNode(newAVL,10)
newAVL = insetNode(newAVL,15)
newAVL = insetNode(newAVL,20)
newAVL = deleteNode(newAVL, 15)
levelOrderTraversal(newAVL)
