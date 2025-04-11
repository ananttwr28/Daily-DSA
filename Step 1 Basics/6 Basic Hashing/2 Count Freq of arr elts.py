''' 
Count frequency of each element in the array on 3/4/25

https://takeuforward.org/data-structure/count-frequency-of-each-element-in-the-array/

Problem

Problem statement: Given an array, we have to find the number of occurrences of each element in the array.

Brute Force Solution - Run two for loop in arr for every item and count and add in dict maintain a visited dict also.

'''
#------------ M1 -------------------------------------
# TC of this Brute Force solution is O(N^2), SC = O(N)

'''

def count_elt_occ(arr):
    count_dict = {}   # SC O(N) or less
    visited_dict = {}   # SC O(N) == no. of arr elts

    for i in range(0, len(arr)):       # TC O(N) 
        if visited_dict.get(arr[i], 0) == 0:  # TC O(1) for checking and inserting in dict
            visited_dict[arr[i]] = 1
            count = 0
            for j in range(0, len(arr)):    # TC O(N) 
                if arr[j] == arr[i]:
                    count += 1
            count_dict[arr[i]] = count
            
    return count_dict

arr = [1, 2, 1, 3, 2]
count_dict = count_elt_occ(arr)

print(count_dict)

'''

#------------ M2 Using Map one iteration -------------------------------------

'''
def count_elt_occ(arr):
    count_dict = {}   # SC O(N) or less

    for i in range(0, len(arr)):       # TC O(N) 
        if count_dict.get(arr[i], 0) == 0:
            count_dict[arr[i]] = 1
        else:
            count_dict[arr[i]] += 1
    return count_dict

arr = [1, 2, 1, 3, 2]
count_dict = count_elt_occ(arr)

print(count_dict)
'''

# If you're doing index-based swaps where the index is derived from the value of the list, be very cautious — mutation during evaluation can bite.

# Use temporary variables to store intermediate values/indexes for safety.


arr = [2, 3, 2, 3, 5]
i = 0

while(i < len(arr)):
    if arr[i] > 0:
        index = arr[i]
        if arr[index-1] > 0:
            arr[i], arr[index-1] = arr[index-1], -1
        else:
            arr[i] = 0
            arr[index-1] += -1
    else:
        i += 1

for i in range(len(arr)):
    arr[i] = abs(arr[i])
print(arr)


# arr[i], arr[(arr[i])-1] = arr[(arr[i])-1], -1