#AVL tree
class node:#class for tree node
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        self.height=1#if single node is there then height will be one
        
def insert(root,super):
    if not root:
        return node(super)
    if  super<root.value:
        root.left=insert(root.left,super)
    else:
        root.right=insert(root.right,super)
    root.height=1+max(ght(root.left),ght(root.right))    
    BF=getBF(root)#BF=balance factor
    #RR rotation
    if BF>1 and super<root.left.val:
        return rightRotate(root)
    #RL rotation
    if BF>1 and super>root.left.val:
        root.left=leftRotate(root.left)
        return rightRotate(root)
    #LL rotation
    if BF<-1 and super >root.right.value:
        return leftRotate(root)
    #LR rotation
    if BF<-1 and super<root.right.value:
        root.right=rightRotate(root.right)
        return leftRotate(root)
    return root

def ght(root):
    if not root:
        return 0
    return root.height
def getBF(root):
    if not root:
        return 0
    return ght(root.left)-ght(root.right)
def leftRotate(B):
    B=A.right
    temp=B.left
    
    B.left=A
    A.right=temp
    return B
def rightRotate(A):
    B=A.left
    temp=B.right
    B.right=A
    A.left=temp
    
    A.height=1+max(ght(A.left),ght(A.right))
    B.height=1+max(ght(B.left),ght(B.right))
    
    return B
def inorder(root):#print the data in inorder formate
    if root==None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)
    
if __name__=="__main__":
    vl=[19,99,75,7,21,34,38,27,134,100,29,0,12,17,143]#vl=value list
    for i in vl:
        root=insert(root,i)

print(insert(root,super))
print(ght(root))
print(getBF(root))
print(leftRotate(B))
