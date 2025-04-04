def SelectionSort(nums):

    for i in range(len(nums)-1):
        minipos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minipos]:
                minipos = j

        temp = nums[i]
        nums[i]= nums[minipos]
        nums[minipos]= temp

        