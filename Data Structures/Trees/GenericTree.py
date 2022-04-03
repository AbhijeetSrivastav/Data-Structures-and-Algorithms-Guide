# General Tree


class TreeNode:
    def __init__(self, data) -> object:
        self.data = data
        self.children = []
        self.parent = None  

    def addChild(self, child):
        child.parent = self
        self.children.append(child)
    
    def getLevel(self):
        level = 0
        parent = self.parent

        while parent:
            level += 1
            parent = parent.parent
        return level
    
    def visualizeTree(self):
        spaces = "  " * self.getLevel()
        prefix = "|__"
        print(spaces + prefix + self.data)

        if self.children:
            for child in self.children:
                child.visualizeTree()