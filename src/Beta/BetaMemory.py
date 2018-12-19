from src.Beta.ReteNode import ReteNode
from src.Beta.Token import Token


class BetaMemory(ReteNode):
    def __init__(self, parent):
        super().__init__(parent)
        self.items = []

    def leftActivation(self, token, workingMemoryElement):
        newToken = Token(token, workingMemoryElement)
        self.items.append(newToken)
        for child in self.children:
            child.leftActivation(newToken)

    def isBetaMemory(self):
        return True

    @staticmethod
    def buildOrShareBetaMemoryNode(parent):
        for child in parent.children:
            if child.isBetaMemory():
                return child
        betaMemory = BetaMemory(parent)
        betaMemory.updateNewNodeWithMatchesFromAbove()
        return betaMemory

    def updateNewNodeWithMatchesFromAbove(self):
        for item in self.parent.alphaMemory.items:
            for token in item.workingMemoryElement.tokens:
                self.leftActivation(token, item.workingMemoryElement)
