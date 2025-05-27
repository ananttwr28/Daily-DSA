'''
Arrays - Medium
Sort an array of 0s, 1s and 2s 27/5/25
https://takeuforward.org/data-structure/sort-an-array-of-0s-1s-and-2s/

'''

'''
------------ Brute Force -------------- TC - O(2N), SC - O(3) = O(1)

Approach - Two iteration and Hashmap or 3 variables to store Count
'''

'''
def sort_arr_0s_1s_2s(nums):
    n = len(nums)
    counts = {}

    for i in range(0, n):      # TC O(N) 
        counts[nums[i]] = counts.get(nums[i], 0) + 1
    j = 0

    # TC - all these combined run for O(N)
    while counts.get(0, 0) > 0:
        nums[j] = 0
        j+=1
        counts[0]-=1
    while counts.get(1, 0) > 0:
        nums[j] = 1
        j+=1
        counts[1]-=1
    while counts.get(2, 0) > 0:
        nums[j] = 2
        j+=1
        counts[2]-=1
    return nums
'''

'''
------------ Optimised -------------- TC - O(N), SC - O(1)

Approach - Three pointers, Dutch National Flag (DNF)
'''

def sort_arr_0s_1s_2s(nums):
    n = len(nums)

    left, mid, high = 0, 0, n-1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left+=1
            mid+=1      

        elif nums[mid] == 1:
            mid+=1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high-=1
    return nums

if __name__ == "__main__":
    nums = [1,0,2,1,0,2,1,0,2]
    sorted_nums = sort_arr_0s_1s_2s(nums)
    print(f"The sorted arr is: {sorted_nums}")