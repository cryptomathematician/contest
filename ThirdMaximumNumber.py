nums = [1,1,2]

if len(set(nums))>=3:
    firstRemoval = [i for i in nums if i!= max(nums)]
    secondRemoval = [i for i in firstRemoval if i!= max(firstRemoval)]
    print(max(secondRemoval))
else:
    print(max(nums))





