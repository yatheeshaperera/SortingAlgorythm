userlist=[]

while True:
    try:
        userinput=int(input("Enter number "))
        userlist.append(userinput)
        if userinput==0:
            userlist.remove(0)
            break
    except ValueError:
        print("Enter a valid input")
        
count=len(userlist)-1

if count==0:
    print("No numbers to sort")
else:
    for x in range (count):
        swapped = False
        for i in range(0,count):
            if userlist[i]>userlist[i+1]:
                userlist[i],userlist[i+1]=userlist[i+1],userlist[i]
                swapped=True
        if not swapped:
            break
print(userlist)