n,k,x= list(map(int, input().split()))
numbers = list(map(int, input().split()))

r = n -k
j= 0
for i in range(r):
    j+=numbers[i]

m = j+ (x*k)

print(m)