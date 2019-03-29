class node:
    def __init__(self,ele):
        self.ele=ele
        self.next=None
class linklist:
    def __init__(self):
        self.head=None
    def insertbeg(self,ele):
        self.ele=ele
        newnode=node(self.ele)
        if self.head==None:
            self.head=newnode
            self.head.next=self.head
        else:
            newnode.next=self.head
            self.head=newnode
            
    def insertend(self,ele):
        self.ele=ele
        newnode=node(self.ele)
        posi=self.head
        if self.head==None:
            self.head=newnode
        else:
          while posi.next!=None:
            posi=posi.next
          newnode.next=self.head
          posi.next=newnode
          
    def insertmid(self,ele,pos):
        self.ele=ele
        self.pos=pos
        posi=self.head
        newnode=node(self.ele)
        position=0
        if self.pos==0:
            self.insertbeg(self.ele)
            return
        for i in range(self.pos-1):
            if posi.next!=None:
                posi=posi.next
            else:
                position=1
                print('index Error')
                break
        if position!=1:
           newnode.next=posi.next
           posi.next=newnode
        
        
    def deletebeg(self):
        if self.head==None:
            print('NO noad')
            return
        self.head=self.head.next
    def deletend(self):
        if self.head==None:
            print('NO noad')
            return
        pos=self.head
        while pos.next.next!=None:
            pos=pos.next
        pos.next=None
    def deleteelement(self,ele):
        if self.head==None:
            print('NO noad')
            return
        pos=self.head
        self.ele=ele
        if self.head.ele==self.ele:
            self.head=self.head.next
        else:
          while pos.next!=None and self.ele!=pos.ele:
            if pos.next.ele==self.ele:
                pos.next=pos.next.next
                break
            pos=pos.next
        
       

           
                   
    def find(self,ele):
        self.ele=ele
        pos=self.head
        while pos.next!=None:
            if self.ele==pos.ele:
                print('found')
                break
            pos=pos.next
        else:
            if pos.ele==self.ele:
                print('found')
            else:
                print('Not found')
    def travers(self):
        pos=self.head
        while pos.next!=None:
            print(pos.ele)
            pos=pos.next
        print(pos.ele)


