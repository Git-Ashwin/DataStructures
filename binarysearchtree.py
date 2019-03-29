class tree:
    def __init__(self,ele=None):
        self.ele=ele
        self.left=None
        self.right=None
    
def insert(root,ele):
    if root==None:
        root=tree(ele)
    elif root.ele<ele:
        root.right=insert(root.right,ele)
    else:
        root.left=insert(root.left,ele)
    return root
def find(root,ele):
    if root.ele==ele:
        return root
    elif root.ele<ele:
        return find(root.right,ele)
    elif root.ele>ele:
       return find(root.left,ele)
def findmin(root):
    pos=root
    while pos.left!=None:
        pos=pos.left
    return pos
def deleteleaf(root):
   if root:
    if root.left==None and root.right==None:
        return None
    root.left=deleteleaf(root.left)
    root.right=deleteleaf(root.right)
   return root
def delete(root,ele):
   if root==None:
       return None
   elif root.ele<ele:
       root.right=delete(root.right,ele)
   elif root.ele>ele:
       root.left=delete(root.left,ele)
   else:
    if root.left==None:
       temp=root.right
       root=None
       return temp
    elif root.right==None:
        temp=root.left
        root=None
        return temp
    else:
      temp=findmin(root.right)
      root.ele=temp.ele
      root.right=delete(root.right,temp.ele)
   return root

    
   
    
    
    



def inorder(root):
    if root:
        inorder(root.left)
        print(root.ele)
        inorder(root.right)

a=tree(11)
for i in [5,15,3,13,4]:
    insert(a,i)
inorder(a)
print()
delete(a,15)
inorder(a)


