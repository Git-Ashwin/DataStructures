class node:
    def __init__(self,ele):
        self.ele=ele
        self.next=None
class circularlinklist:
    def __init__(self):
        self.head=None
    def insertbeg(self,ele):
        newnode=node(ele)
        if self.head==None:
            self.head=newnode
            self.head.next=self.head
        else:
            pos=self.head
            while pos.next!=self.head:
                pos=pos.next
            newnode.next=self.head
            self.head=newnode
            pos.next=self.head
    def insertend(self,ele):
        newnode=node(ele)
        if self.head==None:
            self.head=newnode
            self.head.next=self.head
        else:
            pos=self.head
            while pos.next!=self.head:
                pos=pos.next
            newnode.next=self.head
            pos.next=newnode
    def deletebeg(self):
        if self.head==None:
            print('No node') 
        elif self.head.next==self.head:
            self.head=None
        else:
            pos=self.head
            while pos.next!=self.head:
                pos=pos.next
            self.head=self.head.next
            pos.next=self.head
    def deleteelement(self,ele):
        pos=self.head
        if pos.ele==ele:
            self.deletebeg()
            return
        while pos.next!=self.head:
            if pos.next.ele==ele:
                break
            pos=pos.next
        if pos.next==self.head:
            self.deleteend()
            return
        pos.next=pos.next.next
    def insertelement(self,posi,ele):
        newnode=node(ele)
        pos=self.head
        if pos==0:
            self.insertbeg(ele)
            return
        try:
            for i in range(posi-1):
                pos=pos.next
            newnode.next=pos.next
            pos.next=newnode
        except:
            self.insertend(ele)
        else:
            pass
            
        
        
    def deleteend(self):
        if self.head==None:
            print('No node') 
        elif self.head.next==self.head:           
            self.head=None
        else:
            pos=self.head
            while pos.next.next!=self.head:
                pos=pos.next
            pos.next=self.head
#yeald----generator
    def traverse(self):
        pos=self.head
        while pos.next!=self.head:
            yield pos.ele
            pos=pos.next
        yield pos.ele
a=circularlinklist()
a.insertbeg(10)
a.insertend(40)
a.insertbeg(20)
a.insertbeg(30)
a.insertelement(4,100)
for i in a.traverse():
    print(i)
print()

a.deleteelement(40)

for i in a.traverse():
    print(i)
           