from collections import Counter

number_of = int(input())
for _ in range(number_of):
    n= int(input())
    a = list(map(int, input().split()))
   
    counts = Counter(a)

    loop = dict(counts)
    j=0
    m=0
    for i in a :
        if i == n:
            j+=1
        elif i == 0:
            m+=1
    if len(a) == j:
        print(-1)
    elif len(a)==m:
        print(0)
    
    if len(a) != j and len(a) != m:
        r=[]
        for key,value in loop.items():
            r.append(value)
        
        q=max(r)
        if r.count(max(r))> 1:
            print(n-q)
        else:
            print(q)
            





