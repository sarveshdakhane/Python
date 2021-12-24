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
        Pointer=self.head
        
        while Pointer is not None:
            Next=Pointer.next
            Pointer.next=Prev
            Prev=Pointer 
            Pointer=next
        self.head =Prev





ele1=Node(1)

NL= NumberList()
NL.head=ele1


NL.InsertItem(Node(2))
NL.InsertItem(Node(3))
NL.InsertItem(Node(4))
NL.InsertItem(Node(5))
NL.ReverseLinkList()

Head=NL.head
while Head is not None:
    #print(Head.val)
    Head=Head.next




