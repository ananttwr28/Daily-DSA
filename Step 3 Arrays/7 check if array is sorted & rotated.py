nums = [2,1,3,4]
# n = len(nums)

def reverse(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

def rotate(nums, n, k):
    reverse(nums, 0, n-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)

def is_sorted(nums, n):
    for i in range(1, n):
        if nums[i-1] > nums[i]:
            return False
    return True

def check(nums) -> bool:
    n, k = len(nums), -1
    for i in range(1, n):
        if nums[i-1] > nums[i]:
            k = i
        if k != -1:
            break
    if k != -1:
        k = n-k
        rotate(nums, n, k)
        is_nums_sorted = is_sorted(nums, n)
    
        return is_nums_sorted
    else: # already sorted
        return True

ans = check(nums)
print(ans)