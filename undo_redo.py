class stack:
    def __init__(self):
          self.ls=[]
    def push(self,a):
        self.a=a
        self.ls=self.ls+[self.a]
    def pop(self):
        b=self.ls[-1]
        self.ls=self.ls[:-1]
        return b
    def isempty(self):
        return len(self.ls)==0
a1=stack()
a2=stack()
a=input('enter the string.....')
for i in a:
    a1.push(i)
def undo():
    if a1.isempty():
        print('unable to undo..')
    else:
        b=a1.pop()
        a2.push(b)
def redo():
    if a2.isempty():
        print('unable to redo....')
    else:
        c=a2.pop()
        a1.push(c)

        print(''.join(a1.ls))
    else:
        break
