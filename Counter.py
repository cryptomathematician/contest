from collections import Counter
nums = [3,2,3]
counts = Counter(nums)

loop = dict(counts)
print(loop)


for key,value in loop.items():
    if value> len(nums)/2  :
        print(key)