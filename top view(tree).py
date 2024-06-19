class node_data:
    def __init__(self,Node,HKey):
        self.node=Node
        self.hkey=HKey

def topview(root):        
    temp=node_data(root,0) 
    Q=[temp]
    Q.append(None)
    Key_Dict = {}
    while len(Q) != 0:
        curr = Q.pop(0)
        
        if curr == None:
            if len(Q) == 0:
                break
            else:
                Q.append(None)
        else:
            if curr.hkey not in Key_Dict.keys():
                Key_Dict[curr.hkey] = curr.node.value
            
            if curr.node.left != None:
                temp = node_data(curr.node.left,curr.hkey-1)
                Q.append(temp)
            
            if curr.node.right != None:
                temp = node_data(curr.node.right,curr.hkey+1)
                Q.append(temp)
    for i in sorted(Key_Dict):
        print(Key_Dict[i])
    print(Key_Dict)
topview(root)