
class Node:
    def __init__(self , value =None):
        self.value = value
        self.link =None

class singlylinklist:
    def __init__(self):
        self.Head=None

    def Insert_at_start(self, NewNode):
        newnode=Node(NewNode)
        if self.Head != None:
            newnode.link=self.Head
            self.Head=newnode

    def Insert_at_end(self, NewNode):
        newnode=Node(NewNode)
        if self.Head != None:
            printvalue=self.Head
            while printvalue.link is not None:
                  printvalue=printvalue.link
            printvalue.link=newnode

    def Delete_Node_By_Value(self,TargetNode):
        if self.Head !=None:
            if self.Head.value == TargetNode:
                temp= self.Head
                self.Head=temp.link
                temp=None
                return
            current =self.Head
            while current.link != None:
                if current.link.value == TargetNode:
                    temp =current.link
                    current.link = temp.link
                    temp=None
                    return
                current =current.link
            print("Element is not found in our list")



    def listprint(self):
        printvalue=self.Head
        while printvalue.link is not None:
            print(printvalue.value)
            printvalue=printvalue.link

# Crating the Linklist
Playlist=singlylinklist()
Playlist.Head=Node("Arijit Singh")

# Creating second node
n2= Node("Atif Aslam")
Playlist.Head.link=n2

# Creating third node
n3 = Node("Mohit Chauhan")
n2.link=n3

# Print LinkList
Playlist.listprint()

# Insert Node At Start
print("\n")
for i in range(1,5):
    Playlist.Insert_at_start("Hare {}".format(i))
Playlist.listprint()


# Insert Node At End
print("\n")
for i in range(1,5):
    Playlist.Insert_at_end("Krishna {}".format(i))
Playlist.listprint()


print("\n")
Playlist.Delete_Node_By_Value("Atif Aslam")
Playlist.listprint()