class Stack:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
e="[3+7{52/11(3+5)}"
S=Stack()
OB="[{("
CB=")}]"
count=0
for i in e:
    if i in OB:
        S.push(i)
    if i in CB:
        x=S.pop()
        if x=="(" and i == ")":
            pass
        elif x=="["and i == "]":
            pass
        elif x=="{" and i == "}":
            pass
        else:
            count=1
            break
if count==0 and S.size()==None:
    print("valid")
else:
    print("invalid")
