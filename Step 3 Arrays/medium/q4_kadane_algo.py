'''
Arrays - Medium
Kadane's Algorithm : Maximum Subarray Sum in an Array 28/5/25
https://takeuforward.org/data-structure/kadanes-algorithm-maximum-subarray-sum-in-an-array/

'''

'''
------------ Optimised (Kadane's Algo) -------------- TC - O(N), SC - O(1)
'''

import sys

def find_max_subarr_sum(nums):
    n = len(nums)
    max_sum = -sys.maxsize-1    # == -9*10^18, lowest 64 bit signed int, n=10^5, n[i]=-10^4, sum_arr = -10^5*4 setting INT_MIN type in py for int, else can also use -float('inf'), but it is for float, systems maximum -1 as -ve 0 doesnt exist -2^64 for 64 bit system

    curr_sum=0
    for i in range(0, n):
        curr_sum += nums[i]

        max_sum = max(max_sum, curr_sum)

        if curr_sum < 0:
            curr_sum = 0

    return max_sum


if __name__ == "__main__":
    nums = [-2,2,-1,1]
    max_sum = find_max_subarr_sum(nums)
    print(f"The maximum subarray sum is: {max_sum}")