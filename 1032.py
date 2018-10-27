a=int(input())
l=[]
d=0
for i in range(a):
    b=input()
    if i==0:
        d=len(b)
        for u in range(d):
             l.append(b[u])
    if i!=0:
        for q in range(d):
            if b[q] == l[q]:
                pass
            if b[q] != l[q]:
                l[q]="?"
for i in range(len(l)):
    print(l[i],end="")
