''' 
remove duplicates from sorted array 24/4/25

https://takeuforward.org/data-structure/remove-duplicates-in-place-from-sorted-array/

'''
# BruteForce Approach --> TC O(N^2), SC O(N)

'''

-- Run loop from 0 to n-1 --> TC O(N)

-- check if the arr element is in the new list if not append it --> searching in new list is O(N) TC and append is O(1) SC is O(N) length of new list

-- if not in new list: --> this does linear search and returns true or False

'''

# Better Approach  --> TC O(N), SC O(2N) (for set+list)

'''

seen = set()
-- In this instead of checking in new list we will check by creating a set(unordered in py) its TC is O(1)
-- Run loop from 0 to n-1 --> TC O(N), check if num not i seen then seen.add(num), newlist.append(num)
-- we can add in the same org list also if we are allowed to make changes in org data then SC will be O(N)

'''

# Optimised Approach, in place --> TC O(N), SC O(1)

arr = [2,2,2]
n = len(arr)
i = 0

for j in range(1, n):      # i will track unique elements and j will check all the elts if elt is not equal to unique elt at i then will increase i and insert j at that pos.
    if arr[j] != arr[i]:
        i += 1
        arr[i] = arr[j]

print(i+1)  