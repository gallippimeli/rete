class Token:
    def __init__(self, parent, workingMemoryElement, node):
        self.workingMemoryElement = workingMemoryElement
        self.parent = parent
        self.node = node
        self.children = []

    def addChildren(self, token):
      self.children.insert(0, token)

    def removeChildren(self, token):
      self.children.remove(token)

    @staticmethod
    def makeToken(node, parentToken, workingMemoryElement):
        token = Token(parent = parentToken, workingMemoryElement = workingMemoryElement, node = node)
        parentToken.addChildren(token)
        workingMemoryElement.addToken(token)
        return token

    def deleteTokenAndDescendants(self):
        while len(self.children) != 0:
            self.children[0].deleteTokenAndDescendants()
        self.node.items.remove(self)
        self.workingMemoryElement.removeToken(self)
        self.parent.removeChildren(self)
