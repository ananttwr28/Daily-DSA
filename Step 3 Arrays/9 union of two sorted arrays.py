''' 
union of two sorted arrays (elts in union will be in asc order) 4/5/25

https://takeuforward.org/data-structure/union-of-two-sorted-arrays/

'''

# ------------ Brute Force -------------- 

'''

arr1, arr2 = [5,4,3,2,1], [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3]
n, m = len(arr1), len(arr2)
union_arr, seen = [], set()

for i in range(n):          # ------- TC O(N)
    if arr1[i] not in seen:     # ------- TC O(1)
        seen.add(arr1[i])       # ------- SC O(N)
        union_arr.append(arr1[i])   # ------- SC O(N)
for i in range(m):        # ------- TC O(M)
    if arr2[i] not in seen:    # ------- TC O(1)
        seen.add(arr2[i])      # ------- SC O(M)
        union_arr.append(arr2[i])       # ------- SC O(M)
union_arr.sort()     # TC ------- O((N+M)log(N+M)), SC ------- O((N+M))
print(union_arr)     

"""
Total TC --- O(N) + O(M) + O((N+M)log(N+M)) = O((N+M)log(N+M))
Total SC --- O(2N) + O(2M) + O((N+M)) = O(2N)/O(2M)
"""

'''

# ------------ Optimal -------------- 

arr1, arr2 = [0,0,0,0,0,1,1,2], [1,1,1,1,1,1,1,1,1,1,2,2,2,3,3,3]
# arr1, arr2 = [], [2, 2, 2, 3]
n, m = len(arr1), len(arr2)
union_arr= []     # SC O(N+M)
i, j = 0, 0


while i < n and j < m:          # TC O(N+M)
    if arr1[i] < arr2[j]:
        if len(union_arr) == 0 or arr1[i] != union_arr[-1]:
            union_arr.append(arr1[i])
        i+=1
    elif arr1[i] > arr2[j]:
        if len(union_arr) == 0 or arr2[j] != union_arr[-1]:
            union_arr.append(arr2[j])
        j+=1
    else:
        if len(union_arr) == 0 or arr2[j] != union_arr[-1]:
            union_arr.append(arr2[j])
        i+=1
        j+=1

while i < n:
    if len(union_arr) == 0 or arr1[i] != union_arr[-1]:
        union_arr.append(arr1[i])
    i+=1

while j < m:
    if len(union_arr) == 0 or arr2[j] != union_arr[-1]:
        union_arr.append(arr2[j])
    j+=1

print(union_arr)



"""
Total TC --- O(N+M)
Total SC --- O(N+M)

"""





