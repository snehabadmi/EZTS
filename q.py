class Queue:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
q=Queue()
q.push(10)
q.push(20)
q.push(30)
print(q.items)
print(q.pop())
print(q.items)
print(q.size())