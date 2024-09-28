
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
if __name__ == '__main__':
    s = Stack()
    print (s.is_empty())
    s.push(10)
    s.push(13)
    s.push('dan')
    print (s)
    print (s.pop())
    print(s)
    print (s.size())