l=[]
for i in range(10):
    a=int(input())
    b=a%42
    if b not in l:
        l.append(b)
print(len(l))
