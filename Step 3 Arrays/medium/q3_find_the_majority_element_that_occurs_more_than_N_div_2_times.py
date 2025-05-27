'''
Arrays - Medium
Find the Majority Element that occurs more than N/2 times 27/5/25
https://takeuforward.org/data-structure/find-the-majority-element-that-occurs-more-than-n-2-times/

'''

'''
------------ Optimised -------------- TC - O(N), SC - O(1)

Approach - Majority Element will not get cancelled out by rest as it has freq of > floor(N/2) Moore’s Voting Algorithm
'''

def find_majority_element(nums):
    n = len(nums)
    leader, c = 0, 0
    for i in range(0, n):
        if c == 0:
            leader = nums[i]
            c = 1
        elif nums[i] == leader:     # small mistake fix elif here not if, bcz after resetting leader and adding the same nums[i] count will again inc the count and ans will be wrong
            c += 1
        else:
            c -= 1
    return leader


if __name__ == "__main__":
    nums = [0,1,1,0,1,1,2,2]
    majority_element = find_majority_element(nums)
    print(f"The majority element is: {majority_element}")