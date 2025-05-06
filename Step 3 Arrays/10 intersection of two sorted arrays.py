''' 
intersection of two sorted arrays (elts in intersection will be in asc order) 5/5/25

https://takeuforward.org/data-structure/intersection-of-two-sorted-arrays/

'''

# ------------ Brute Force -------------- TC O(min(N, M))*O(M)/O(N) = O(N^2), SC O(min(N, M)) (when each elt exists less will be less)

'''
approach - 
iterate over arr1 and check if it exists in 2nd arr then insert in the new list if it doesnt exists (we want only uniques in intersection)
return (since both arrs are sorted no need of sorting again)
'''

'''

arr1, arr2, intersection_arr = [1, 2, 3, 3, 4, 5, 6], [3, 3, 5], []
n, m = len(arr1), len(arr2)

for i in range(n):      # TC O(N)    
    if arr1[i] in arr2:  # TC O(M)
        if len(intersection_arr) == 0 or intersection_arr[-1] != arr1[i]:
            intersection_arr.append(arr1[i])

print(intersection_arr)

'''

# ------------ Optimal -------------- TC O(N+M) when both arrs are unequal, SC O(min(N, M)) (when each elt exists)

'''
approach - 
run two pointers from start of each arrs till anyone reaches end
since they are sorted if some elt is less or greater meaning not equal so they are not present in other increment ptrs
if equal check if not in new list then add and increment both since we only wanted uniques 
code finishes when one of two arrs ends
'''

arr1, arr2, intersection_arr = [1, 2, 3, 3, 4, 5, 6], [3, 3, 5], []
n, m = len(arr1), len(arr2)
i, j = 0, 0

while i < n and j < m:         
    if arr1[i] < arr2[j]:        # meaning the a2 elt might be somewhere ahead in a1 thus i++
        i+=1
    elif arr1[i] > arr2[j]:        # meaning the a1 elt might be somewhere ahead in a2 thus j++
        j+=1
    else:        # == case we want any one not duplicated add and increase both
        if len(intersection_arr) == 0 or intersection_arr[-1] != arr1[i]:        # insert 
            intersection_arr.append(arr1[i])
        i+=1
        j+=1
# if any of i j finishes means all the common elts are checked 
print(intersection_arr)

