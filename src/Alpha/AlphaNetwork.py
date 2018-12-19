from src.Alpha.AlphaMemory import AlphaMemory
from src.Alpha.TestNode import TestNode
from src.Beta.BetaMemory import BetaMemory
from src.Beta.JoinNode import JoinNode
from src.Beta.PNode import PNode
from src.Beta.TestAtJoinNode import TestAtJoinNode
from src.InputFiles.Constants import Constants


class AlphaNetwork():
    def __init__(self):
        self.topNode = TestNode(True, "Top Node")
        self.workingMemory = []
        self.productionNodes=[]

    def addCondition(self, condition):
        self.topNode.addCondition(condition)

    def addWorkingMemoryElement(self, workingMemoryElement):
        self.workingMemory.append(workingMemoryElement)
        self.activateConstantTestNode(self.topNode, workingMemoryElement)

    def activateConstantTestNode(self, node, workingMemoryElement):
        if not node.isTopNode:
            if workingMemoryElement.attribute == node.name:
                self.activateChildConstantTestNode(node, workingMemoryElement)
            if workingMemoryElement.value == node.name:
                node.alphaMemory.addIfCompare(workingMemoryElement)
        else:
            self.activateChildConstantTestNode(node, workingMemoryElement)

    def activateChildConstantTestNode(self, node, workingMemoryElement):
      for child in node.children:
        self.activateConstantTestNode(child, workingMemoryElement)
    
    def buildOrShareAlphaMemory(self, condition):
        currentNode = self.topNode
        currentNode = self.buildOrShareConstantTestNode(currentNode, condition)
        if currentNode.alphaMemory is not None:
            return currentNode.alphaMemory
        alphaMemory = AlphaMemory(condition)
        currentNode.alphaMemory = alphaMemory
        for workingMemoryElement in self.workingMemory:
            alphaMemory.addIfCompare(workingMemoryElement = workingMemoryElement)
        return alphaMemory

    @staticmethod
    def buildOrShareConstantTestNode(parent, condition):
        testNode = parent.addCondition(condition)
        return testNode

    def addProduction(self, Rule):
        lhs = Rule.getConditions()
        currentNode = self.topNode
        earlierConditions = []
        tests = currentNode.addCondition(lhs[0])
        alphaMemory = self.buildOrShareAlphaMemory(lhs[0])
        currentNode = JoinNode.buildOrShareJoinNode(currentNode, alphaMemory, tests)
        for i in range(1,len(lhs)):
            currentNode = BetaMemory.buildOrShareBetaMemoryNode(currentNode)
            earlierConditions.append(lhs[i-1])
            tests = TestAtJoinNode.getJoinTestFromCondition(lhs[i],earlierConditions)
            alphaMemory = self.buildOrShareAlphaMemory(lhs[i])
            currentNode = JoinNode.buildOrShareJoinNode(currentNode, alphaMemory, tests)
        productionNode = PNode(currentNode,Rule)
        currentNode.children.append(productionNode)
        productionNode.updateNewNodeWithMatchesFromAbove()
        self.productionNodes.append(productionNode)

    def getWorkingMemoryContent(self):
        knowString= "Los resultados son:\n"
        for workingMemoryElement in self.workingMemory:
            knowString += " - "+ str(workingMemoryElement.attribute) + " : "
            if Constants.hasKey(workingMemoryElement.attribute):
                knowString += str(Constants.getConstant(workingMemoryElement.attribute, workingMemoryElement.value))
            else:
                knowString += str(workingMemoryElement.value)
            knowString += "\n"
        return knowString