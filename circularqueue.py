class circularqueue:
    def __init__(self,a):
        self.limit=a
        self.ls=[]
        for i in range(self.limit):
            self.ls.append(None)
        self.front=None
        self.rear=None
    def isempty(self):
        if self.front == None and self.rear==None:
            return 1
        return 0
    def isfull(self):
        if self.front==0 and self.rear==(self.limit-1):
            return 1
        elif self.rear<self.front:
               if self.rear==self.front-1:
                return 1
        return 0
    def enqueue(self,a):
        self.a=a
        if self.isempty():
            self.rear=self.front=0
            self.ls[self.rear]=self.a
        elif self.isfull():
            print('overflow')
        else:
            self.rear=(self.rear+1)%self.limit
            self.ls[self.rear]=self.a
            self.isfull()
    def dequeue(self):
        if self.isempty():
            print('underflow')
        if self.front==self.rear:
            self.front=self.rear=None
        else:
            self.front=(self.front+1)%self.limit
            if self.front==self.limit:
                self.front=self.rear=None


'''b=int(input('enter the no players....'))

c=1
v=0
m=[i for i in range(c,b+1)]
a=circularqueue(len(m))
for i in m:
    a.enqueue(i)
while not v:
  for j in range(int(input('enter the no of spin'))):
    b=a.ls[a.front]
    a.dequeue()
    a.enqueue(b)
  b1=a.ls[a.front]
  a.dequeue()
  print(b1)
  v=a.isempty()'''
  



      