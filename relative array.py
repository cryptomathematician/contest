arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 =[2,1,4,3,9,6]
j = sorted(arr1)
r = []
for i in arr2:
    for j in arr1:
        if j== i:
            r.append(j)
l = []
for k in arr1:
    if k not in arr2:
        l.append(k)

m = sorted(l)

print(r+m)


