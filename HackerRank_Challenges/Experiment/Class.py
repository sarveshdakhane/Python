class Base1 ():
      
    def __init__(self):
        self.fatherName="Rajendra"
        self.General="Dakhane"

class Base2 (Base1):

    def __init__(self,Name):
         self.YourName=Name
         Base1.__init__(self)
       
    def print_msg(self):
        print("Child {} {} {}".format(self.YourName,self.fatherName,self.General))


if __name__ == "__main__":
        Obj=Base2("sarvesh")
        print(Obj.General)
        Obj.print_msg()