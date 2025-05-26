'''
Longest Subarray with given Sum K(Positives+Negatives) 26/5/25
https://takeuforward.org/arrays/longest-subarray-with-sum-k-postives-and-negatives/

'''

'''
------------ Brute Force -------------- TC - O(N^3), SC - O(1)

Approach - 
Sum of every possible subarray and find the max length
1. 1st loop to choose starting index for each subarray (from 0 to n-1)
2. 2nd loop to choose ending index for each subarray (from 0 to n-1)
3. 3rd loop to calculate sum of subarray from i to j
i = 0  --> sub arrays will be i=0 to j=0, i=0 to j=1, i=0 to j=2, i=0 to j=3,...

'''

'''
def find_max_subarray_length(nums, k):
    n = len(nums)

    max_subarray_length = 0

    for i in range(0, n):       # starting index of each subarray
        for j in range(i, n):          # ending index of each subarray
            curr_subarray_sum = 0
            for m in range(i, j+1):             # subarr a[i...j] included
                curr_subarray_sum += nums[m]
            
            if curr_subarray_sum == k:
                max_subarray_length = max(max_subarray_length, (j-i+1))

    return max_subarray_length
'''


'''
------------ Better -------------- TC - O(N^2), SC - O(1)
Approach - 
Sum of every possible subarray and find the max length
1. 1st loop to choose starting index for each subarray (from 0 to n-1)
2. 2nd loop to choose ending index for each subarray (from 0 to n-1) and will be calculating sum of subarr in the same loop
3. we will not use 3rd loop, curr_sub_arr_sum = prev_sub_arr_sum + curr_elt i.e. arr[j]

'''

'''

def find_max_subarray_length(nums, k):
    n = len(nums)

    max_subarray_length = 0

    for i in range(0, n):       # starting index of each subarray
        curr_subarray_sum = 0       # resetting sum to 0 after each i, bcz checking i=0 to j=0 and checking if sum ==k then i=0 to j=1 will not reset inside j loop bcz we want sum of i=0 to j=1 then we want sum of j=0 also, will reset only for subarr starting from new i index, means new starting idx
        for j in range(i, n):          # ending index of each subarray
            curr_subarray_sum += nums[j]
            
            if curr_subarray_sum == k:
                max_subarray_length = max(max_subarray_length, (j-i+1))

    return max_subarray_length

'''

'''
------------ Optimised -------------- TC - O(N), SC - O(N)
'''


def find_max_subarray_length(nums, k):
    prefix_sum_dict = {}  
    # prefix_sum_dict = {0:-1}     # storing initial sum=0 and idx=-1, if any subarr starting from 0 whose sum becomes equal k and sum-k = 0 wont be present to prevent this
    n = len(nums)

    prefix_sum, max_subarray_length = 0, 0

    for i in range(0, n):  
        prefix_sum += nums[i]    
        
        if prefix_sum == k:     # for subarrs starting from 0 the above 0,-1 case 2+3+5=10 but 10-10 wont be in dict but its valid subarr and its len will be i+1 for 0 based indexing
            max_subarray_length = max(max_subarray_length, i+1)
        if prefix_sum-k in prefix_sum_dict:
            start_idx = prefix_sum_dict[prefix_sum-k]       # start idx of the subarr of sum=k will be the value of p_s-k means after that idx
            max_subarray_length = max(max_subarray_length, i-start_idx) # not doing +1 here bcz already taking the start idx of x-k in above step so no need
        if prefix_sum not in prefix_sum_dict:
            prefix_sum_dict[prefix_sum] = i         # only for +ve, -ve & 0, map will overwrite the idx with new one we want longest, so if idx exist we will not do anything, for +ves sum will keep on increasing and this case wont come

    return max_subarray_length

if __name__ == "__main__":
    nums, k = [-1, 1, 1], 1     # do dry run slowly in pen paper and each concept will be clear for above approach 26/5
    max_subarray_length = find_max_subarray_length(nums, k)
    print(f"The length of the longest subarray is: {max_subarray_length}")