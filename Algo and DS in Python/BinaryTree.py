from typing import Counter


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
    
    def PreOrder(self,root):
        if root == None:
            return
        print(root.data)
        self.PreOrder(root.left)
        self.PreOrder(root.right)
    
    def IterativePreOrder(self, root):
        if root is None:
            return
        stack=[]
        stack.append(root)
        while stack:
            current = stack.pop()
            print(current.data)

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    def PostOrder(self,root):
        if root ==None:
            return
        self.PostOrder(root.left)
        self.PostOrder(root.right)
        print(root.data)

    def IntervativePostOrder(self,root):
        if root is None:
            return
        stack=[]
        stack.append(root)
        while stack:
            if root.left:      
               stack.append(root.left)
            if root.right:
               stack.append(root.right)
            root = stack.pop()
            print(root.data)

   
    def deletion(self,root,ele):
        if not root:
           return None
        
        if ele < root.data:
            root.left = self.deletion(root.left,ele)
        elif ele > root.data:
            root.right = self.deletion(root.right,ele)
        else:
            if not (root.left or root.right):
                root =None
            elif root.right:
                root.data=self.successor(root)
                root.right=self.deletion(root.right,root.data)
            else:
                root.data = self.predecessor(root)
                root.left = self.deletion(root.left,root.data)
        
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
for ele in [10,5,25,2,7,23,30]:
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

print("\nPreorder printing of Tree\n")

b.PreOrder(root)


print("\nIteravative method result Preorder printing of Tree\n")

b.IterativePreOrder(root)


print("\nPosteorder printing of Tree\n")

b.PostOrder(root)

print("\nIteravative method result Postorder printing of Tree\n")

b.IntervativePostOrder(root)

b.DeleteLeadNode(root,30)
print("\n Inorder Tree After Deletion")
b.inorder(root)

