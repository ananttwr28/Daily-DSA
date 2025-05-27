'''
Arrays - Medium
Two Sum : Check if a pair with given sum exists in Array 27/5/25
https://takeuforward.org/data-structure/two-sum-check-if-a-pair-with-given-sum-exists-in-array/

'''

'''
------------ Brute Force -------------- TC - O(N^2), SC - O(1)

Approach - Nested Loops
'''

'''
def find_indices(nums, target):
    n = len(nums)

    for i in range(0, n-1):       # starting index of each pair
        for j in range(i+1, n):          # ending index of each pair
            pair_sum = 0
            
            pair_sum = nums[i] + nums[j]
            
            if pair_sum == target:
                return [i, j]

    return [-1, -1]

'''

'''
------------ Better -------------- TC - O(N), SC - O(N)

Approach - Hashing/ Hashmap
'''

'''
def find_indices(nums, target):
    n = len(nums)
    rem_dict = {}

    for i in range(0, n):       # starting index of each pair
        if target - nums[i] in rem_dict:
            return [rem_dict[target-nums[i]], i]
        rem_dict[nums[i]] = i

    return [-1, -1]

'''

'''
------------ Optimised (When Arr is sorted/ or just have to return yes/no) -------------- TC - O(NlogN), SC - O(1)

Approach - Two pointers

This is optimised solution when given Arr is sorted else have to sort arr and this is valid only for telling if there exist a pair with target sum, else idx gets distorted after sorting will have to use new list of tuple to store old idxs then sort
'''

'''
def find_indices(nums, target):
    n = len(nums)
    left, right = 0, n-1

    nums.sort()

    while left < right:
        if nums[left] + nums[right] == target:
            return "YES"
        elif nums[left] + nums[right] < target:
            left += 1
        else:
            right -= 1

    return "NO"

'''

'''
------------ Solution - Unsorted Arr and have to return indices -------------- TC - O(NlogN), SC - O(N)

Approach - New list + Sort + Two pointers
In efficient use hashing instead of this

'''

def find_indices(nums, target):
    n = len(nums)
    new_list = []

    for i in range(0, n):    # TC O(N)
        new_list.append((nums[i], i))   # SC O(N)

    # sort the new list based on element not on idx --> TC O(NlogN)
    # use two pointer --> TC O(N)

if __name__ == "__main__":
    nums, target = [2,6,5,8,11], 14  
    indices = find_indices(nums, target)
    print(f"The indices of pair with given target sum: {indices}")