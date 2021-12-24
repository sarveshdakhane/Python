x=input()

N,K= x.split(" ")

StreetNumber=input().split(" ")

pathResult=[]

for i in range(int(N)):
    firstElement=int(StreetNumber[1])
    temp=firstElement
    for j in range(int(N)):      
        Conditon= int(StreetNumber[j])-int(StreetNumber[i])
        if i != j and Conditon <= int(K) and Conditon >= 1:
            temp+= StreetNumber[j]
    pathResult.append(temp)
    temp=0


print(pathResult)