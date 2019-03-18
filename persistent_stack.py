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
    p0 = Stack()
    p1 = Push(p0,1)
    p2 = Push(p1,2)
    p3 = Push(p2,3)
    p4 = Push(p1,4)
    print(Top(p2))
    p5 = Pop(p2)
    print(Top(p5))
    p6 = Push(p2,5)
    print(Top(p4))
    p7 = Push(p4,6)
    print(Size(p6))
    p8 = Push(p3,7)
    p9 = Pop(p3)
    print(Top(p7))
    print(p8)
    print(p9)

if __name__ == '__main__':
    main()

