a=int(input())
l=[]
ll=[]
l=list(map(int,input().split()))
ll=list(map(int,input().split()))
re=0
for i in range(a):
    c=min(l)*max(ll)
    re+=c
    l.remove(min(l))
    ll.remove(max(ll))
print(re)
