class ItemInAlphaMemory():
    def __init__(self, workingMemoryElement, alphaMemory):
        self.previous = None
        self.next = None
        self.alphaMemory = alphaMemory
        self.workingMemoryElement = workingMemoryElement
