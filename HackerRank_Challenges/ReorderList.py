class Node:
    def __init__(self,val=None):
        self.val=val
        self.next=None


class NumberList:
    def __init__(self):
        self.head=None

    def InsertItem(self,ele):
        Temp=self.head
        while Temp.next is not None:
            Temp=Temp.next
        Temp.next=ele

    def ReverseLinkList(self):
        Prev=None
        Pointer = self.head
        while (Pointer is not None):
            Next=Pointer.next
            Pointer.next=Prev
            Prev=Pointer 
            Pointer=Next
        self.head =Prev

    def ReorderList(self):
        leng=[]
        LastPoniter = self.head 
        while LastPoniter is not None:
               leng.append(LastPoniter)
               LastPoniter = LastPoniter.next
        
        
        
        li=len(leng)
        if li % 2 == 0:
            length=(li/2)+1
        else:
            length=(li/2)+0.5

        poniter=self.head
        Next=None
        for i in range(0,int(length)):
                    Next=poniter.next 
                    poniter.next=leng[-(i+1)]
                    NewNeibour=poniter.next
                    NewNeibour.next=Next
                    poniter=Next

        LastNode=leng[int(length)-1]
        LastNode.next=None


NL= NumberList()
NL.head=Node(1)
NL.InsertItem(Node(2))
NL.InsertItem(Node(3))
NL.InsertItem(Node(4))
NL.InsertItem(Node(5))
NL.InsertItem(Node(6))
NL.InsertItem(Node(7))

NL.ReorderList()


Head=NL.head
while Head is not None:
    print(Head.val)
    Head=Head.next

