import persistent_stack as stack

class QueueCell:
    def __init__(self, stack, removed):
        self.stack = stack
        self.removed = removed

def Queue():
    return QueueCell(None, 0)

def Enqueue(q, n):
    return QueueCell(stack.Push(q.stack,n), q.removed)

def Dequeue(q):
    return QueueCell(q.stack, q.removed + 1)

def Size(q):
    return stack.Size(q.stack) - q.removed

def First(q):
    return stack.Kth(q.stack, q.removed + 1)

def Kth(q, k):
    return stack.Kth(q.stack, q.removed + k)

def main():
    q0 = Queue()
    q1 = Enqueue(q0, 1)
    q2 = Enqueue(q1, 2)
    q3 = Enqueue(q2, 3)
    q4 = Dequeue(q3)
    
    print(First(q3))
    print(First(q4))

if __name__ == '__main__':
    main()
