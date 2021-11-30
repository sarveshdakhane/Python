stackslist=[]

for i in range(0,5):
    stackslist.append("Student {}".format(i))

for i in stackslist:
    print(i)

stackslist.pop()
print("\n")

for i in stackslist:
    print(i)

stackslist.pop()
print("\n")


for i in stackslist:
    print(i)

stackslist.pop(0)
print("\n")


for i in stackslist:
    print(i)


print("Peek Operation (last element of list) \n" + stackslist[-1])
