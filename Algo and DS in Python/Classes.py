class ABC:
    First=0
    Second=0

    def __init__(self , A , B):
        self.A=A
        self.B=B
    
    def square(self):
        A=self.A
        B=self.B
        print("{}".format(A**B))


def main():
    print("Main Called")
    abc = ABC(25,24)
    print(abc.First)
    print(abc.square)


if __name__=="__main__":
    main()                  



        
