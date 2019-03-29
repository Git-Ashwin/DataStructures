class minheap:
    def __init__(self):
        self.ls=[0]
        self.size=0


    def perup(self,i):
        while i//2>0:
           if self.ls[i//2]>self.ls[i]:
                  self.ls[i//2],self.ls[i]=self.ls[i],self.ls[i//2]

           i=i//2

    def perdown(self,i):
        pass

    def insert(self,ele):
        self.ls.append(ele)
        self.size+=1
        self.ls[0]=self.size
        self.perup(self.size)


    def minchild(self,i):
        if i*2+1>self.size:
            return i*2
        else:
            if self.ls[i*2]>self.ls[i*2+1]:
                return i*2+1
            else:
                return i*2

    
    def buildheap(self,a):
        self.ls=self.ls+a[:]
        self.size=self.size+len(a)
        self.ls[0]=self.size
        i=self.size
        while i>0:
            self.perup(i)
            i-=1

    def delete(self):
        ret = self.ls[-1]
        self.ls.pop()
        self.size=0
        a=self.ls[1:]
        self.ls=[0]
        self.buildheap(a)
        return ret

a=minheap()
a.buildheap([7,10,10,20,3,4,49,50,50])

print(a.ls)




