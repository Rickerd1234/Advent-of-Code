# Imports
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

class Dir():
    def __init__(self, name, parent):
        self.name = name
        self.contains = set()
        self.parent = parent

    def addItem(self, obj):
        if obj in self.contains:
            print(f"ERROR: {obj.name} already exists in {self.name}")
            return
        self.contains.add(obj)

    def getDir(self, dir_name):
        result = [dir for dir in self.contains if dir.name == dir_name]
        if len(result) == 0:
            print(f"ERROR: {dir_name} does not exist in {self.name}")
            return
        return result[0]

    def getDirSize(self):
        return sum(file.size for file in self.contains if type(file) == File) + sum(dir.getDirSize() for dir in self.contains if type(dir) == Dir)
        
    def getRoot(self):
        return self.parent.getRoot() if self.parent is not None else self

    def getParent(self):
        return self.parent if self.parent is not None else self

class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size

# Part 1
def p1(inp):
    currentDir = Dir("/", None)
    dir_list = [currentDir]
    for line in inp:
        if line[0] == "$":
            command = line[2:]
            
            if command[:2] == "cd":
                arg = command[3:]
                if arg == "..":
                    currentDir = currentDir.getParent()
                elif arg == "/":
                    currentDir = currentDir.getRoot()
                else:
                    currentDir = currentDir.getDir(arg)
                
        else:
            info, name = line.split(" ")

            if info.isnumeric():
                currentDir.addItem(File(name, int(info)))
            else:
                dir = Dir(name, currentDir)
                currentDir.addItem(dir)
                dir_list.append(dir)

    print(sum(dir.getDirSize() if dir.getDirSize() < 100_000 else 0 for dir in dir_list))
    return dir_list

# Part 2
def p2(inp, dir_list):
    total = 70_000_000
    current = dir_list[0].getDirSize()
    unused = total - current
    required = 30_000_000
    free_up = required - unused
    print(min(dir.getDirSize() for dir in dir_list if dir.getDirSize() > free_up))


# Run main functions
o1 = p1(inp)
p2(inp, o1)