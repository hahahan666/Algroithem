class BiTree():
    def __init__(self, value):
        self.value = value  
        self.left = None
        self.right = None

    def setValue(self, newvalue):
        self.value = newvalue

    def setLeft(self, leftvalue=''):
        leftNode = BiTree(leftvalue)
        self.left = leftNode

    def setRight(self, rightvalue=''):
        rightNode = BiTree(rightvalue)
        self.right = rightNode

    def getValue(self):
        return self.value

    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
