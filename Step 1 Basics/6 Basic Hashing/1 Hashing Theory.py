''' 
Hashing Code Implementation by me on 1/4/25

https://takeuforward.org/hashing/hashing-maps-time-complexity-collisions-division-rule-of-hashing-strivers-a2z-dsa-course/


Problem

Given an array of integers: [1, 2, 1, 3, 2] and we are given some queries: [1, 3, 4, 2, 10]. For each query, we need to find out how many times the number appears in the array. For example, if the query is 1 our answer would be 2, and if the query is 4 the answer will be 0. 

Solution - Run a for loop in arr for every query item and count and add in dict.

'''

# TC of this Brute Force solution is O(N^2)

def count_elt_occ(arr, n):
    count = 0
    for i in range(0, len(arr)):       # TC O(N)
        if arr[i] == n:
            count += 1
    return count

arr = [1, 2, 1, 3, 2]
query = [1, 3, 4, 2, 10]
dict = {}   # SC O(N)

for i in range(0, len(query)):        # TC O(N)
    count = count_elt_occ(arr, query[i])     # TC O(N)
    dict[query[i]] = count
print(dict)

