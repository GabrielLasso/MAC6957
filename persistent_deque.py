class DequeCell:
    def __init__(self, value, depth, parent, _jmp):
        self.value = value
        self.depth = depth
        self.parent = parent
        self._jmp = _jmp

def Deque():
    return (None, None)

def Front(d):
    return d[0].value

def Back(d):
    return d.secont.value

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

d0 = Deque()
d1 = PushBack(d0,3)
d2 = PushBack(d1,4)
d3 = PushFront(d2,2)
d4 = PushFront(d3,1)
d5 = PopBack(d3)
d6 = PopBack(d5)
d7 = PushFront(d6,9)
d8 = PopFront(d6)
d9 = PushFront(d8,6)
