import random as ran
import time


def swap(a,F,S):
    a[F],a[S]=a[S],a[F]

def QShort(a,start,end):
    i=start 
    j=end-1
    p=end
    while i<=j:

        while a[i]<a[p]:
            i+=1
        while (j>=start) and (a[j]>=a[p]):
            j-=1
        if i<=j:
            swap(a,i,j)
    
    swap(a,i,p)
    if(start<i-1):
        QShort(a,start,i-1)

    if(end>i+1):
        QShort(a,i+1,end)



start= time.time()
#a=[1,5,1,3,2,3,4,5,66,88]
a=[]

for i in range(1,1900):
    a.append(ran.randint(1,100))
QShort(a,0,len(a)-1)

end = time.time()
#print([x for x in a])
print("Execuation time was {}".format(end-start))



