import persistent_stack as stack
import sys

class QueueCell:
    def __init__(self, stack, removed):
        self.stack = stack
        self.removed = removed

    def __str__(self):
        p = self.stack
        string = ""
        while (p != None and p.size > self.removed):
            string += str(p.value) + " "
            p = p.previous
        return string

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
    versions = []
    line = sys.stdin.readline()
    while (line):
        tokens = line.replace('(', ',').replace(')', ',').split(',')
        tokens = list(filter(lambda tk: bool(tk), map(lambda tk: tk.strip(), tokens)))
        if (tokens):
            functionName = tokens[0]
            args = list(map(lambda arg: int(arg), tokens[1:]))
            if (functionName == "Queue"):
                versions.append(Queue())
            elif (functionName == "Enqueue"):
                versions.append(Enqueue(versions[args[0]],args[1]))
            elif (functionName == "Dequeue"):
                versions.append(Dequeue(versions[args[0]]))
            elif (functionName == "Size"):
                print(Size(versions[args[0]]))
            elif (functionName == "First"):
                print(First(versions[args[0]]))
            elif (functionName == "Kth"):
                print(Kth(versions[args[0]], args[1]))
            elif (functionName == "Print"):
                print(versions[args[0]])
        line = sys.stdin.readline()

if __name__ == '__main__':
    main()
