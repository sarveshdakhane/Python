


class ATM:
    def __init__(self,WA,AB):
        self.WithdrawAmount=WA
        self.AccountBalance=AB
        self.Withdraw()
    
    def Withdraw(self):
        if self.WithdrawAmount % 5 == 0 and (self.WithdrawAmount+ + 0.50) <= self.AccountBalance:
               print("{:.2f}".format((self.AccountBalance-self.WithdrawAmount)-0.50))      
        else:
            print("{:.2f}".format(self.AccountBalance))
          
 

inputArray=input().split(" ")
if len(inputArray) > 0:
    WA=float(inputArray[0])
    AB=float(inputArray[1])
    obj=ATM(WA,AB)
    