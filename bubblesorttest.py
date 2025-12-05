l=[] #list name
while True: #runs until the below condition true
    num=int(input(""))
    if num>0:
        l.append(num)
    else:
        break
loop=0
a=0 #variable
b=1 #variable
cache=0
while loop<len(l):
    a=0
    b=1
    while b<len(l):
        if l[a]>l[b]:
            cache=l[a]#15
            l[a]=l[b]
            l[b]=cache
        a=a+1
        b=b+1
    loop=loop+1
    continue
print(l)



            
