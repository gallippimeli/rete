from src.Beta.ReteNode import ReteNode


class PNode(ReteNode):
    def __init__(self, parent, rule):
        super().__init__(parent)
        self.rule = rule
        self.ruleWmes = []

    def isTopNode(self):
        return False

    def updateNewNodeWithMatchesFromAbove(self):
        parent = self.parent
        if parent.isBetaMemory():
            for token in parent.items:
                print("updateNewNodeWithMatchesFromAbove", token)
        if parent.isJoinNode():
            savedListOfChildren = parent.children
            parent.children = [self]
            for item in parent.alphaMemory.items:
                parent.rightActivation(item.workingMemoryElement)
                self.ruleWmes.append(item.workingMemoryElement)
            parent.children = savedListOfChildren

    def getRuleName(self):
        return self.rule.getName()

    def isRuleUsed(self,workingMemory):
        for workingMemoryElement in workingMemory:
            if self.rule.hasAction(workingMemoryElement.attribute, [workingMemoryElement.symbol, workingMemoryElement.value]):
                return True
        return False

    def getGetWme(self):
        for workingMemoryElement in self.ruleWmes:
            print(workingMemoryElement)