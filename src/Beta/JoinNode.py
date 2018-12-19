from src.Beta.ReteNode import ReteNode
from src.Beta.Token import Token


class JoinNode(ReteNode):
    def __init__(self, parent, alphaMemory, tests):
        super().__init__(parent)
        self.alphaMemory = alphaMemory
        self.name = alphaMemory.condition.name
        self.value = alphaMemory.condition.value
        self.tests = tests
        self.children = []
        self.isTopNode = False

    def rightActivation(self, workingMemoryElement):
        if self.isBetaMemory():
            for t in self.parent.items:
                if self.performJoinTests(t, workingMemoryElement):
                    for child in self.children:
                        child.leftActivation(t, workingMemoryElement)

    def leftActivation(self, token):
        for item in self.alphaMemory.items:
            if self.performJoinTests(token, item.workingMemoryElement):
                for child in self.children:
                    child.leftActivation(token, item.workingMemoryElement)

    def performJoinTests(self, t, workingMemoryElement):
        raise Exception()

    def isJoinNode(self):
        return True

    @staticmethod
    def buildOrShareJoinNode(parent, alphaMemory, tests):
        for child in parent.children:
            if child.isJoinNode():
                if child.alphaMemory == alphaMemory and child.tests == tests:
                    return child
        joinNode = JoinNode(parent, alphaMemory, tests)
        parent.children.insert(0, joinNode)
        alphaMemory.succesors.insert(0, joinNode)
        return joinNode
