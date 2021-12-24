
x=input()
n,k= x.split(" ")
t=[]
count=0

for i in range(int(n)):
    t.append(input())

for i in t:
    if int(i) % int(k) ==0:
        count +=1

print(count)
