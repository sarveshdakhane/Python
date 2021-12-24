class Node:
    def __init__(self, Value=None):
        self.Previous = None
        self.Value = Value
        self.Next = None


class DoubleLinkList:
    def __init__(self):
        self.Head = None
    
    def Insert_at_begining(self,ele):
        NewNode=Node(ele)
        if self.Head == None:
            self.Head=NewNode
        else:
            NewNode.Next=self.Head
            self.Head.Previous=NewNode
            self.Head=NewNode
    def Insert_at_ending(self,ele):
        NewNode=Node(ele)
        p=self.Head
        if self.Head == None:
            self.Head=NewNode
        else:
            while p.Next is not None:
                p=p.Next
            p.Next=NewNode
            NewNode.Previous=p
            NewNode.Next=None

    def PrintDoubleLinkList(self,TargetList):
            p=TargetList.Head
            while p is not None:
                print("Value : {} \n". format(p.Value))
                p=p.Next





DoubleLinkList = DoubleLinkList()
DoubleLinkList.Head = Node("Prem")
Node1 = Node("Ram")
Node2 = Node("Sham")
DoubleLinkList.Head.Next=Node1
DoubleLinkList.Head.Next.Previous=DoubleLinkList.Head
DoubleLinkList.Head.Next.Next=Node2
DoubleLinkList.PrintDoubleLinkList(DoubleLinkList)
print("After insterting Element at first (i.e. 'Rahul') \n")
DoubleLinkList.Insert_at_begining("Rahul")
DoubleLinkList.PrintDoubleLinkList(DoubleLinkList)
print("After insterting Element at End (i.e. 'Rushi') \n")
DoubleLinkList.Insert_at_ending("Rushi")
DoubleLinkList.PrintDoubleLinkList(DoubleLinkList)


