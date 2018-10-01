x=int(input())
l=[64,32,32,16,16,8,8,4,4,2,2,1]
num=0
for i in range(len(l)):
    if l[i]<=x:
        if x-l[i]>=0:
            x-=l[i]
            num+=1
print(num)
