import persistent_stack as stack

class Queue:
    def __init__(self, stack, removed):
        self.stack = stack
        self.removed = removed

def queue():
    return Queue(None, 0)

def enqueue(q, n):
    return Queue(stack.push(q.stack,n), q.removed)

def dequeue(q):
    return Queue(q.stack, q.removed + 1)

def size(q):
    return stack.size(q.stack) - q.removed

def get_first(q):
    return stack.kth(q.stack, q.removed + 1)

def kth(q, k):
    return stack.kth(q.stack, q.removed + k)

q0 = queue()
q1 = enqueue(q0, 1)
q2 = enqueue(q1, 2)
q3 = enqueue(q2, 3)
q4 = dequeue(q3)

print(get_first(q3))
print(get_first(q4))

