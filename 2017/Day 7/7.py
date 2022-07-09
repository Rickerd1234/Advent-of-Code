# Imports
from statistics import mode
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

class Program:
    def __init__(self, name_weight, children=""):
        self.name, weight = name_weight.split(" ")
        self.weight = int(weight[1:-1])
        self.children = children.split(", ")
        self.child_nodes = []
        self.parent = None

    def setParent(self, parent):
        self.parent = parent
    
    def getRoot(self):
        if self.parent:
            return self.parent.getRoot()
        else:
            return self

    def updateChildren(self, nodes):
        self.child_nodes = [node for node in nodes if node.name in self.children]

    def getCompleteWeight(self):
        return self.weight + sum([child.getCompleteWeight() for child in self.child_nodes])

    def getUnbalancedNode(self):
        w = mode([child.getCompleteWeight() for child in self.child_nodes])
        if all([child.getCompleteWeight() == w for child in self.child_nodes]):
            return self
        else:
            return [child for child in self.child_nodes if child.getCompleteWeight() != w][0].getUnbalancedNode()

    def __repr__(self):
        return f"{self.name} ({self.weight}) - {len(self.children)}"

# Part 1
def p1(inp):
    leaves = [Program(node) for node in inp if "->" not in node]
    nodes = [Program(*node.split(" -> ")) for node in inp if "->" in node]
    combined = leaves + nodes
    findName = lambda name: [node for node in combined if node.name == name][0]
    for node in nodes:
        for child in node.children:
            findName(child).setParent(node)
    root = combined[0].getRoot()
    print(root.name)
    return root, combined

# Part 2
def p2(inp, o1):
    root, nodes = o1
    for node in nodes:
        node.updateChildren(nodes)
    unbalanced = root.getUnbalancedNode()
    fam_mode = mode([child.getCompleteWeight() for child in unbalanced.parent.child_nodes])
    print(fam_mode - unbalanced.getCompleteWeight() + unbalanced.weight)
    return


# Run main functions
o1 = p1(inp)
p2(inp, o1)
