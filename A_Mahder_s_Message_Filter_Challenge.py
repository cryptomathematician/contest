t = int(input())
for _ in range(t):
    n = int(input())
    s= input()
    r= []
    for i in range(0,len(s)):
        if s[-i-1]== ')':
            r.append(s[-i-1])
        else:
            break
    

 
    k = n-len(r)
    j = len(r)
    if j > k :
        print('Yes')
    else:
        print('No')

