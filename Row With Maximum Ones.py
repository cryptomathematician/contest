from collections import Counter
mat = [[0,1],[1,0]]
listings = [Counter(i) for i in mat]
print(listings)
j = [dict(k) for k in listings]
print(j)

r = [m.get(1, 0) for m in j] 
print(r)

w=max(r)

position = r.index(w)

print([position,w])

