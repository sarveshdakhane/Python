class Node:
    def __init__(self,data) -> None:
        self.data= data
        self.left = None
        self.right = None
    
class BST:
    def buildBST(self,root,ele):
        if root == None:
            return Node(ele)
        if ele < root.data:
            root.left = self.buildBST(root.left,ele)
        else:
            root.right =self.buildBST(root.right,ele)
        return root

    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    
    def SearchItem(self,root,ele):
        if root is None or root.data == ele:
            return root
        if root.data > ele:
            return self.SearchItem(root.left,ele)
        return self.SearchItem(root.right,ele)
   
    def FindMaxElement(self,root):
        if root.right is None:
            return root
        return self.FindMaxElement(root.right)
    
    def FindMinElement(self,root):
        if root.left is None:
            return root
        return self.FindMinElement(root.left)
        
        
        


root=None
b=BST()
for ele in [99,10,5,25,90,2,0.5,7,30]:
    root = b.buildBST(root,ele)

b.inorder(root)
print("\n")
Search_result=b.SearchItem(root,0.5)


if Search_result is not None:
    print("{} Yes Present".format("0.5"))
else:
    print("{} Not Found".format("0.5"))

print("\n")

MaxElement=b.FindMaxElement(root)
print("Max element is {} ".format(MaxElement.data))

MinElement=b.FindMinElement(root)
print("Min element is {} ".format(MinElement.data))


