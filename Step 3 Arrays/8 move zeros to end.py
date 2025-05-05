def moveZeroes(nums):
    n = len(nums)
    j = -1
    for i in range(n):
        if nums[i] == 0:
            j = i
            break
    if j != -1:
        for i in range(j+1, n):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j] 
                j+=1


nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)