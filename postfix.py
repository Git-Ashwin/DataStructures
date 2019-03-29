class stack:
    def __init__(self):
        self.ls=[]
    def push(self,a):
        self.a=a
        self.ls.append(self.a)
    def pop(self):
        b=self.ls[:][-1]
        self.ls=self.ls[:-1]
        return b
        
    def peek(self):
        return self.ls[-1]
    def isempty(self):
        if len(self.ls)==0:
            return 1
        return 0
if __name__ == "__main__":
  a=stack()
  b=input('enter the string.....')
  prec={'+':1,'-':1,'*':2,'/':2,'(':-1}
  for i in b:
    if i=='(':
        a.push(i)
    elif i==')':
        while not a.isempty():
          if a.peek() !='(':
            print(a.pop(),end='')
          else:
              break
        a.pop()
    elif i not in ['+','-','*',"/"]:
        print(i,end="")
    else:
        if a.isempty():
            a.push(i)
        else:
            while  (not a.isempty()):
              if prec[i]<=prec[a.peek()]: 
                print(a.pop(),end='')
              else:
                  break
            a.push(i)
  for i in a.ls[::-1]:
    print(i,end='')
