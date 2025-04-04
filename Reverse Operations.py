nums = list(map(int, input().split()))
k=nums[:]
for i in nums:
    r = str(i)[::-1]
    k.append(int(r))
print(k)
    
