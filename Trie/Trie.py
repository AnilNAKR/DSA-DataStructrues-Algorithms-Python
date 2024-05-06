class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofstring = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # Insert String Method
    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endofstring = True
        print("Successfully inserted")
    
    #search for a string in a Trie
    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node

        if currentNode.endofstring == True:
            return True
        else:
            return False

#Delete a string from a Trie
def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False
    
    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endofstring = False
            return False
        else:
            root.children.pop(ch)
            return True
    
    if currentNode.endofstring == True:
        deleteString(currentNode, word, index+1)
        return False

    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False

    



newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
# print(newTrie.searchString("DCD"))
# print(newTrie.searchString("App"))
deleteString(newTrie.root, "App",0)
print(newTrie.searchString("App"))