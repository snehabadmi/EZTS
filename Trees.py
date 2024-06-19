class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def preorder(root):
    if root==None:
        return
    print(root.value)
    preorder(root.left)
    preorder(root.right)
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)
def postorder(root):
    if root==None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value)
if __name__=="__main__":
        
        root=node(1)
        root.left=node(2)
        root.right=node(3)
        root.left.left=node(4)
        root.left.right=node(5)
        root.right.left=node(6)
        root.right.right=node(7)
print("preorder:")
print(preorder(root))
print("inorder:")
print(inorder(root))
print("postorder:")
print(postorder(root))