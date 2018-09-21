l=[]
A,B=input().split()
A=int(A)
B=int(B)
a=[]
b=[]
for u in range(1,A+1):
    if A==1:
        a.append(A)
    if A%u==0:
        a.append(u)
for u in range(1,B+1):
    if B==1:
        b.append(B)
    if B%u==0:
        b.append(u)
for u in range(len(a)):
    for z in range(len(b)):
        if (a[u]*b[z])%A==0:
            if (a[u]*b[z])%B==0:
                l.append(a[u]*b[z])
                break
print(l[0])
