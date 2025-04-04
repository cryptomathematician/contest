from collections import Counter
arr = [1,7,9,5,4,1,2]
j = max(arr)
k = arr.index(j)      
m = Counter(arr[:k])
w =  Counter(arr[k:])
print(w)
print(m)
r = []
for key,value in m.items():
    if value > 1:
        r.append(key)
e = []
for key,value in w.items():
    if value > 1:
        r.append(key)

h, b= arr[:k], arr[k:]

if h!= sorted(h) or b !=  [sorted(b)][::-1]:
   print(False)

elif len(r) == 0 and len(e)==0  and arr[len(arr)-1] !=j and  arr[0]!=j:
    print(True)

else:
    print(False)





