import sys

class DequeCell:
    def __init__(self, value, depth, parent, _jmp):
        self.value = value
        self.depth = depth
        self.parent = parent
        self._jmp = _jmp

    def __str__(self):
        return str(self.value)

def Deque():
    return (None, None)

def Front(d):
    return d[0].value

def Back(d):
    return d[1].value

def swap(d):
    return (d[1], d[0])

def depth(u):
    if (u == None):
        return 0
    return u.depth

def parent(u):
    if (u == None):
        return None
    return u.parent

def LA(u, k):
    startingDepth = depth(u)
    while(startingDepth - depth(u) < k):
        if (startingDepth - depth(u._jmp) < k):
            u = u._jmp
        else:
            u = parent(u)
    return u

def LCA(u, v):
    if (depth(u) > depth(v)):
        u, v = v, u
    v = LA(v, depth(v) - depth(u))
    if (u == v):
        return u
    while (parent(u) != parent(v)):
        if (u._jmp != v._jmp):
            u = u._jmp
            v = v._jmp
        else:
            u = parent(u)
            v = parent(v)
    return parent(u)

def PushFront(d, x):
    if (d[0] == None):
        u = DequeCell(x, 1, None, None)
        return (u, u)
    else:
        jmp = d[0]
        if (d[0]._jmp != None and depth(d[0]) - depth(d[0]._jmp) == depth(d[0]._jmp) - depth(d[0]._jmp._jmp)):
            jmp = d[0]._jmp._jmp
        return (DequeCell(x, depth(d[0]) + 1, d[0], d[0]._jmp), d[1])

def PushBack(d, x):
    return swap(PushFront(swap(d), x))

def PopFront(d):
    if (d[0] == d[1]):
        return Deque()
    elif (LCA(d[0], d[1]) == d[0]):
        return (d[1], LA(d[1], depth(d[1]) - depth(d[0]) - 1))
    else:
        return (parent(d[0]), d[1])

def PopBack(d):
    return swap(PopFront(swap(d)))

def Kth(d, k):
    lca = LCA(d[0], d[1])
    l1 = depth(d[0]) - depth(lca)
    l2 = depth(d[1]) - depth(lca)
    if (k - 1 <= l1):
        return (LA(d[0], k - 1)).value
    else:
        return (LA(d[1], l1 + l2 + 1 - k)).value

def toString(d):
    lca = LCA(d[0], d[1])
    u = d[0]
    v = d[1]
    string = str(u.value)
    while (u != lca):
        u = u.parent
        string += " "
        string += str(u.value)
    secondPart = []
    while (v != lca):
        secondPart.append(str(v.value))
        v = v.parent
    secondPart.reverse()
    string += " " + " ".join(secondPart)
    return string

def main():
    versions = []
    line = sys.stdin.readline()
    while (line):
        tokens = line.replace('(', ',').replace(')', ',').split(',')
        tokens = list(filter(lambda tk: bool(tk), map(lambda tk: tk.strip(), tokens)))
        if (tokens):
            functionName = tokens[0]
            args = list(map(lambda arg: int(arg), tokens[1:]))
            if (functionName == "Deque"):
                versions.append(Deque())
            elif (functionName == "PushFront"):
                versions.append(PushFront(versions[args[0]],args[1]))
            elif (functionName == "PushBack"):
                versions.append(PushBack(versions[args[0]],args[1]))
            elif (functionName == "PopFront"):
                versions.append(PopFront(versions[args[0]]))
            elif (functionName == "Front"):
                print(Front(versions[args[0]]))
            elif (functionName == "Back"):
                print(Back(versions[args[0]]))
            elif (functionName == "Kth"):
                print(Kth(versions[args[0]], args[1]))
            elif (functionName == "Print"):
                print(toString(versions[args[0]]))
        line = sys.stdin.readline()

if __name__ == '__main__':
    main()

