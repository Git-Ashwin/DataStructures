class queue:
    def __init__(self,a):
        self.ls=[]
        self.b=a
    def enqueue(self,a):
        if len(self.ls)==self.b:
            v=self.dequeue()
            print(v,'is poped due to over flow..')

        self.a=a
        self.ls.append(self.a)
    def dequeue(self):
        if self.isempty():
            print('under folw....')
        else:
           b=self.ls[0]
           self.ls=self.ls[1:]
           return(b)
    def isempty(self):
        return len(self.a)==0
    def qsize(self):
        return len(self.ls)

