
string="CanChef123recover111this120file.OrNot11."
es=[]
newlist=""
numbers=[]
flag=0
SumOfEven=0
SumOfOdd=0




for i in range(len(string)):
    es.append(string[i])


for item in es:

    if len(newlist)>1 and item == 0:
            newlist=newlist+item
    elif item ==0:
        continue
    elif item.isdigit():
        newlist=newlist+item
    else:
        flag=1  
    if flag==1  and len(newlist)>1:
        numbers.append(newlist)   
        newlist=""  
    flag=0       
    
for i in numbers:
    if int(i)%2 == 0:
        SumOfEven = SumOfEven + int(i)
    else:
        SumOfOdd = SumOfOdd + int(i)

   
if (SumOfEven - SumOfOdd) == 0:
     print("Yes")
else:
     print("No")


