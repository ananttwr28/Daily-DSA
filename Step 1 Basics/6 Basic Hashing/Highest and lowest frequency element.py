''' 
Find the highest/lowest frequency element 4/4/25

https://takeuforward.org/arrays/find-the-highest-lowest-frequency-element/

M1 -- Brute Force Solution - Run two for loop in arr for every item and count and add in dict maintain a visited dict also.

'''

# ----------- M2 using map ------------------------

# arr = [10,5,10,15,10,5]
# hash_map = {}   # SC O(N)
# max_freq, max_freq_ele = 0, 0
# min_freq, min_freq_ele = 999, 0

# for i in range(len(arr)):        # TC O(N)
#     if hash_map.get(arr[i], 0) == 0:
#         hash_map[arr[i]] = 1
#     else:
#         hash_map[arr[i]] += 1

# for key, value in hash_map.items():   # TC O(N)
#     if value > max_freq:
#         max_freq = value
#         max_freq_ele = key
#     if value < max_freq:
#         min_freq = value
#         min_freq_ele = key

# print("Max frequency element is:", max_freq_ele, sep=" ")
# print("Min frequency element is:", min_freq_ele, sep=" ")


# M3 LC Ques

nums = [1,4,8,13]
k=5

nums.sort(reverse= True)
i, freq =0, 1
j = i+1

while j < len(nums):
    if k > 0:
        diff = nums[i] - nums[j]
        if diff > k:
            i+=1
            j+=1
        elif diff == k:
            freq=max(freq, j-i+1)
            i+=1
            j+=1 
        else:
            k-= diff
            freq=max(freq, j-i+1)
            j+=1
    
# return freq

print(freq)