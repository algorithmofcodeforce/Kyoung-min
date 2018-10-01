num=int(input())
l=[]
l=input().split()
for i in range(1,num):
    a=[]
    for u in range(1,int(l[i])+1):
        if int(l[0])%u==0:
            if int(l[i])%u==0:
                a.append(u)
    b=int(int(l[0])/int(max(a)))
    c=int(int(l[i])/int(max(a)))
    b=str(b)
    c=str(c)
    print(b+"/"+c)
