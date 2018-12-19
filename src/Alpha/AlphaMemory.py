from src.Alpha.ItemInAlphaMemory import ItemInAlphaMemory

class AlphaMemory:
    def __init__(self, condition):
        self.condition = condition
        self.items = []
        self.succesors = []

    def addIfCompare(self, workingMemoryElement):
        if self.condition.compareValue(workingMemoryElement.value):
            newItem = ItemInAlphaMemory(workingMemoryElement, self)
            self.items.insert(0, newItem)
            workingMemoryElement.alphaMemsItems.insert(0,newItem)
            for child in self.succesors:
                child.rightActivation(workingMemoryElement)

