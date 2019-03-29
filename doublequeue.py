class doublequeue:
    def __init__(self,a):
        self.a=a
        self.ls=[]
    def dequeueright(self):
        if self.isempty():
            print('under flow')
        else:
            b=self.ls[-1]
            self.ls=self.ls[:-1]
            return b
    def dequeleft(self):
        if self.isempty():
            print('under flow')
        else:
            b=self.ls[0]
            self.ls=self.ls[1:]
            return b
    def enqueueright(self,a):
        if len(self.ls)==self.a:
            print('overflow...')
        else:
            self.aa=a
            self.ls.append(self.aa)
    def enqueueleft(self,a):
        if len(self.ls)==self.a:
            print('overflow...')
        else:
            self.bb=[a]
            self.ls=self.bb+self.ls
    def isempty(self):
        return len(self.ls)==0
a=doublequeue(int(input('enter the limit....')))
for i in range(int(input('enter the no of operations......'))):
     b=input('enter the type of operation....')
     if 'appendright' in b:
           a.enqueueright(b.split()[1])
           print(a.ls)
     if 'appendleft' in b:
           a.enqueueleft(b.split()[1])
           print(a.ls)
     if 'dequeueleft' in b:
           a.dequeleft()
           print(a.ls) 
     if 'dequeueright' in b:
           a.dequeueright()
           print(a.ls) 
    
