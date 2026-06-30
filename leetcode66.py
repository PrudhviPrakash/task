digits=[1,2,3]
a=0
b=[]
for i in digits:
    a=a*10+i
a+=1
c=str(a)
for i in c:
    b.append(int(i))
print(b)
        