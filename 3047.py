l=[]
a,b,c=map(int,input().split())
for a in [a,b,c]:
    l.append(a)
l.sort()
num=input()
for i in range(3):
    if num[i]=="A":
        print(l[0],end=" ")
    elif num[i]=="B":
        print(l[1],end=" ")
    elif num[i] == "C":
        print(l[2],end=" ")
