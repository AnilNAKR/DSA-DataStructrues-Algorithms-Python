class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    #isEmpty() method to check if the stack is empty or not
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    #Time Complexity is - O(1) & S.C is - O(1)
    
    #Push() -> To add elements into the stack
    def push(self,value):
        self.list.append(value)
        return "The element has been successfully inserted"
    
    #Pop() -> To return the 1st element in the stack and delete/pop the element
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()
        
    # Peak() -> to return the top element in the stack
    def peak(self):
        if self.isEmpty():
            return "There is no elements in the stack"
        else:
            return self.list[len(self.list)-1]
    
    #Delete entire stack
    def delete(self):
        self.list = None

customStack = Stack()
# print(customStack.isEmpty())  
customStack.push(1)
customStack.push(2)
customStack.push(3)
# print(customStack.pop())
# print("--------")
print(customStack)
# print(customStack.peak())
customStack.delete()
print(customStack.isEmpty())