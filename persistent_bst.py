import sys

class BSTCell:
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        string = ""
        if (self.left != None):
            string += self.left.__str__() + " "
        string += str(self.value)
        if (self.right != None):
            string += " " + self.right.__str__()
        return string

    def __strdepth__(self, depth):
        string = ""
        string += "  " * depth + str(self.value) + "\n"
        if (self.left != None):
            string += self.left.__strdepth__(depth + 1)
        else:
            string += "  " * (depth + 1) + "None\n"
        if (self.right != None):
            string += self.right.__strdepth__(depth + 1)
        else:
            string += "  " * (depth + 1) + "None\n"
        return string

    def copy(self):
        return BSTCell(self.left, self.right, self.value)

    def isLeaf(self):
        return self.left == None and self.right == None

def BST():
    return None

def Insert(r, x):
    if (r == None):
        return BSTCell(None, None, x)
    copy = r.copy()
    if (x < r.value):
        copy.left = Insert(r.left, x)
    elif (x > r.value):
        copy.right = Insert(r.right, x)
    return copy

def Search(r,x):
    if (r == None):
        return None
    if (r.value == x):
        return x
    if (r.value > x):
        return Search(r.left, x)
    if (r.value < x):
        return Search(r.right, x)

def Min(r):
    while(r.left != None):
        r = r.left
    return r.value

def Delete(r, x):
    if (Search(r, x) == None):
        return r
    new_root = r.copy()
    current_node = new_root
    parent = new_root
    while (current_node.value != x):
        parent = current_node
        if (current_node.value > x):
            current_node = current_node.left.copy()
            parent.left = current_node
        else:
            current_node = current_node.right.copy()
            parent.right = current_node

    node_to_be_deleted = current_node

    if (node_to_be_deleted.isLeaf()):
        if (parent.value > x):
            parent.left = None
        else:
            parent.right = None
        return new_root

    if (node_to_be_deleted.left == None):
        if (node_to_be_deleted == new_root):
            return new_root.right
        parent.right = node_to_be_deleted.right
        return new_root

    node_to_replace = node_to_be_deleted.left.copy()
    node_to_be_deleted.left = node_to_replace
    previous_node = node_to_be_deleted
    while (node_to_replace.right != None):
        previous_node = node_to_replace
        node_to_replace = node_to_replace.right.copy()
        previous_node.right = node_to_replace

    if (node_to_be_deleted.left != node_to_replace):
        previous_node.right = node_to_replace.left
        node_to_replace.left = node_to_be_deleted.left
    node_to_replace.right = node_to_be_deleted.right

    if (node_to_be_deleted == new_root):
        return node_to_replace

    if (parent.value > node_to_replace.value):
        parent.left = node_to_replace
    else:
        parent.right = node_to_replace

    return new_root

def Debug(r):
    print(r.__strdepth__(0))

def main():
    versions = []
    line = sys.stdin.readline()
    while (line):
        tokens = line.replace('(', ',').replace(')', ',').split(',')
        tokens = list(filter(lambda tk: bool(tk), map(lambda tk: tk.strip(), tokens)))
        if (tokens):
            functionName = tokens[0]
            args = list(map(lambda arg: int(arg), tokens[1:]))
            if (functionName == "BST"):
                versions.append(BST())
            elif (functionName == "Insert"):
                versions.append(Insert(versions[args[0]],args[1]))
            elif (functionName == "Delete"):
                versions.append(Delete(versions[args[0]], args[1]))
            elif (functionName == "Search"):
                print(Search(versions[args[0]], args[1]))
            elif (functionName == "Min"):
                print(Min(versions[args[0]]))
            elif (functionName == "Debug"):
                Debug(versions[args[0]])
            elif (functionName == "Print"):
                print(versions[args[0]])
            else:
                print("Command not found")
        line = sys.stdin.readline()

if __name__ == '__main__':
    main()

