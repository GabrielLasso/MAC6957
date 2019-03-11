class Stack:
    def __init__(self, value, size, previous, _jmp):
        self.value = value
        self.size = size
        self.previous = previous
        self._jmp = _jmp
        
    def __str__(self):
        q = self
        string = ""
        while (q != None):
            string += str(q.value) + "\n"
            q = q.previous
        return string

def stack():
    return None

def size(p):
    if (p == None):
        return 0
    return p.size

def push(p, n):
    if (p != None and p._jmp != None and size(p) - size(p._jmp) == size(p._jmp) - size(p._jmp._jmp)):
        return Stack(n, size(p) + 1, p, p._jmp._jmp)
    return Stack(n, size(p) + 1, p, p)

def pop(p):
    return p.previous
    
def get_top(p):
    return p.value

def kth(p, k):
    while (size(p) > k):
        if (size(p._jmp) > k):
            p = p._jmp
        else:
            p = p.previous
    return p.value

# p0 = stack()
# p1 = push(p0,3)
# p2 = push(p1, 5)
# p3 = pop(p2)
# p4 = push(p3, 7)
# p5 = push(p4, 15)
# p6 = push(p5, 10)
# p7 = push(p4, 10)
# p8 = pop(p4)
# 
# print(p6)
# print(get_top(p8))
# print(kth(p6, 2))
# 
