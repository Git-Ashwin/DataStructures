#swaping leaf node in binarysearchtree
def swap(root):
 if root:
  swap(root.left)
  swap(root.right)
  if root.right==None:
      root.right=root.left
      root.left=None
  elif root.left==None:
      root.left=root.right
      root.right=None
  
  elif (root.right.right==None and root.right.left==None) or (root.left.left==None and root.left.right==None):
          root.right,root.left=root.left,root.right
		