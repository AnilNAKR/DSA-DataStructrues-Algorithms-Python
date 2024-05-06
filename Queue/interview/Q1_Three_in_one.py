class MultiStack:
    def __init__(self, stacksize):
        self.numberstacks = 3
        self.customList = [0] * (self.numberstacks * stacksize)
        self.sizes = [0] * self.numberstacks
        self.stacksize = stacksize

    def isFull(self,stacknum):
        if self.sizes[stacknum] == self.stacksize:
            return True
        else:
            return False
    
    def isEmpty(self,stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False
        
    def indexOfTop(self, stacknumber):
        offset = stacknum * self.stacksize
        