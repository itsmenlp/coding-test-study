import sys

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, x):
        self.stack.append(x)
        
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return -1
        
    def size(self):
        return len(self.stack)
    
    def empty(self):
        return 1 if not self.stack else 0
    
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1
        
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    stack = Stack()
    results = []
    
    for _ in range(n):
        command = sys.stdin.readline().strip().split()
        
        if command[0] == "push":
            stack.push(int(command[1]))
        elif command[0] == "pop":
            results.append(str(stack.pop()))
        elif command[0] == "size":
            results.append(str(stack.size()))
        elif command[0] == "empty":
            results.append(str(stack.empty()))
        elif command[0] == "top":
            results.append(str(stack.top()))
            
    sys.stdout.write("\n".join(results) + "\n")
            
