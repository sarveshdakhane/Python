class ABC:
    def __init__(self , A , B):
        self.A=A
        self.B=B
    
    def __str__(self):
        return print("{} + {}".format(self.A, self.B))
    
    def square(self):
        A=self.A
        B=self.B
        print("{}{}".format(A,B))




def main():
    print("Main Called")
    abc = ABC(25,24)
    print(abc)

if __name__=="__main__":
    main()                  



        
