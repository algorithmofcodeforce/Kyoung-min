num=int(input())
l=[1,2,3]
for i in range(num):
    a,b=map(int,input().split())
    for u in range(len(l)):
        if l[u] == a:
            l[u]=b
        elif l[u]==b:
            l[u]=a
print(l[0])
