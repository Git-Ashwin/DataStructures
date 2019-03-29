class node:
    def __init__(self,ele):
        self.ele=ele
        self.right=None
        self.left=None
def inorder(pos):
       
        if pos!=None:
            inorder(pos.left)
            print(pos.ele)
            inorder(pos.right)
def preorder(pos):
       
        if pos!=None:
            print(pos.ele)
            preorder(pos.left)
            preorder(pos.right)
def postorder(pos):
        if pos!=None:
            postorder(pos.left)
            postorder(pos.right)
            print(pos.ele)
a=node(10)
a.right=node(20)
a.right.left=node(15)
a.left=node(30)
a.left.right=node(28)
inorder(a)
