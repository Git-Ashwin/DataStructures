class node:
    def __init__(self,ele):
        self.ele=ele
        self.next=None
        self.prev=None
class dlinklist:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertbeg(self,ele):
        newnode=node(ele)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            pos=self.head
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def insertmid(self,posi,ele):
        pos=self.head
        newnode=node(ele)
        if posi==0:
            self.insertbeg(ele)
            return
        try:
          for i in range(posi-1):
             pos=pos.next
          newnode.prev=pos
          newnode.next=pos.next
          pos.next.prev=newnode
          pos.next=newnode
    
        except:
            self.insertend(ele)
        else:
            pass
    


            
    def insertend(self,ele):
        newnode=node(ele)
        if self.head==None:
            self.head=newnode
            self.tail=newnode
        else:
            pos=self.head
            while pos.next!=None:
                pos=pos.next
            newnode.prev=pos
            pos.next=newnode
            self.tail=newnode
    def deletebeg(self):
        if self.head==None:
            print('No Node')
        else:
            self.head=self.head.next
            self.head.prev=None
    def deleteend(self):
        pos=self.head
        if self.head==None:
            print('No Node')
        else:
           self.tail=self.tail.prev
           self.tail.next=None
    def deletemid(self,ele):
        pos=self.head
        if pos.ele==ele:
            self.deletebeg()
            return
        while pos.next!=None and pos.next.ele!=ele:
            pos=pos.next
        if pos.ele==ele:
           pos.next=pos.next.next
           pos.next.prev=pos
        print('element not found')
      


        
        
        
    def travers(self,s='S'):
        if s=='S':
            pos=self.head
            while pos.next!=None:
                print(pos.ele)
                pos=pos.next
            print(pos.ele)
        else:
            pos=self.tail
            while pos.prev!=None:
                print(pos.ele)
                pos=pos.prev
            print(pos.ele)

    
           
a=dlinklist()
a.insertbeg(5)
a.insertbeg(3)
a.insertend(11)
a.insertmid(0,10)


a.travers()
