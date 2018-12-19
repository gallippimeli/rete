import src.Alpha.AlphaNetwork

from src.Alpha.AlphaNetwork import AlphaNetwork
from src.Alpha.WorkingMemoryElement import WorkingMemoryElement
from src.FowardChain import FowardChain
from src.Knowledge.KnowledgeParser import KnowledgeParser
from src.Rules.RulesParser import RulesParser

rules = RulesParser.getRules("./src/InputFiles/rulesEnfermedades.txt")
knowledge = KnowledgeParser.getKnowledges("./src/InputFiles/knowledgesChikungunia.txt")

fwdChain = FowardChain(rules = rules, knowledge = knowledge)
fwdChain.runReteAlgorithm()

alphaNetwork = AlphaNetwork()
for key in knowledge.getKeys():
    workingMemoryElement = WorkingMemoryElement(key, knowledge.getSymbol(key), knowledge.getValue(key))
    alphaNetwork.addWorkingMemoryElement(workingMemoryElement)
for rule in rules:
    alphaNetwork.addProduction(rule)

print(fwdChain.getUsedRulesContent())
print(alphaNetwork.getWorkingMemoryContent())
