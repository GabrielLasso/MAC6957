import sys

class StackCell:
    def __init__(self, value, size, previous, _jmp):
        self.value = value
        self.size = size
        self.previous = previous
        self._jmp = _jmp
        
    def __str__(self):
        q = self
        string = ""
        while (q != None):
            string += str(q.value) + " "
            q = q.previous
        return string

def Stack():
    return None

def Size(p):
    if (p == None):
        return 0
    return p.size

def Push(p, x):
    if (p != None and p._jmp != None and Size(p) - Size(p._jmp) == Size(p._jmp) - Size(p._jmp._jmp)):
        return StackCell(x, Size(p) + 1, p, p._jmp._jmp)
    return StackCell(x, Size(p) + 1, p, p)

def Pop(p):
    return p.previous
    
def Top(p):
    return p.value

def Kth(p, k):
    while (Size(p) > k):
        if (Size(p._jmp) > k):
            p = p._jmp
        else:
            p = p.previous
    return p.value

def main():
    versions = []
    line = sys.stdin.readline()
    while (line):
        tokens = line.replace('(', ',').replace(')', ',').split(',')
        tokens = list(filter(lambda tk: bool(tk), map(lambda tk: tk.strip(), tokens)))
        if (tokens):
            functionName = tokens[0]
            args = list(map(lambda arg: int(arg), tokens[1:]))
            if (functionName == "Stack"):
                versions.append(Stack())
            elif (functionName == "Push"):
                versions.append(Push(versions[args[0]],args[1]))
            elif (functionName == "Pop"):
                versions.append(Pop(versions[args[0]]))
            elif (functionName == "Size"):
                print(Size(versions[args[0]]))
            elif (functionName == "Top"):
                print(Top(versions[args[0]]))
            elif (functionName == "Kth"):
                print(Kth(versions[args[0]], args[1]))
            elif (functionName == "Print"):
                print(versions[args[0]])
        line = sys.stdin.readline()

if __name__ == '__main__':
    main()

