class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
         

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The BT is full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "The value has been sucessfull inserted"

    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not found"
    
    # PreOrder Traversal
    def PreOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.PreOrderTraversal(index*2)
        self.PreOrderTraversal(index*2 + 1)
    # Inorder Traversal
    def InOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.InOrderTraversal(index * 2)
        print(self.customList[index])
        self.InOrderTraversal(index * 2 + 1)
    
    # Post Order Traversal
    def PostOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.InOrderTraversal(index * 2)
        self.InOrderTraversal(index * 2 + 1)
        print(self.customList[index])
    
    # Level order Traversal
    def LevelOrderTraversal(self, index):
        for i in range(index,self.lastUsedIndex+1):
            print(self.customList[i])
    
    # Delete a node from the python list
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "There is not any node to delete"
        for i in range(1,self.lastUsedIndex):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted"

    #Delete an entire Binary Tree
    def deleteTree(self):
        self.customList = None
        return "The Binary tree has been successfully deleted"

newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
# print(newBT.searchNode("Hot"))
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
# newBT.PreOrderTraversal(1)
# newBT.InOrderTraversal(1)
# newBT.PostOrderTraversal(1)

print(newBT.deleteNode("Tea"))
print(newBT.customList[0])
# print(newBT.deleteTree())
# newBT.LevelOrderTraversal(1)