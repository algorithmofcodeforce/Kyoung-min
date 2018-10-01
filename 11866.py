num, fi = input().split()
num = int(num)
fi = int(fi)
list = []
q = []
for i in range(1, num+1):
    list.append(i)
list.append(" ")
finish = 0
a=1
c=0
while (" " in list):
    for u in range(len(list)):
        if list[u]==" ":
            continue
        if list[u]==0:
            continue
        if a % fi == 0:
            q.append(list[u])
            list[u]=0
            a+=1
        else:
            a += 1
    if len(q)==num:
        list.remove(" ")
for i in range(len(q)):
    if i==0:
        print("<",end="")
    if i==len(q)-1:
        print(q[i],end=">")
    else:
        print(q[i],end=", ")
