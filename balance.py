class balance:
    def __init__(self,a):
        self.a=a
        self.ls=[]
    def push(self,a):
        self.aa=a
        self.ls.append(self.aa)
    def pop(self):
        self.ls=self.ls[:-1]

    def check(self):
        
        for i in self.a:
            if i in ('[','{','('):
                self.push(i)
            elif i==']':
                if self.ls[-1]=='[':
                    self.pop()
                else:
                   return 0
            elif i=='}':
                if self.ls[-1]=='{':
                    self.pop()
                else:
                   return 0
            elif i==')':
                if self.ls[-1]=='(':
                    self.pop()
                else:
                  return 0
        if len(self.ls)==0:
            return 1
        else:
            return 0
a=balance(input())
print(a.check())

            



