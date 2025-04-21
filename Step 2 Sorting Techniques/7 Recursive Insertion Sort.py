''' 
Recursive Insertion Sort Algorithm 21/4/25
https://takeuforward.org/arrays/recursive-insertion-sort-algorithm/

O(N^2) TC and O(2N) = O(N) SC for max fn at once in call stack
'''

arr = [52, 42, 1, 24, 3]
n = len(arr) 

def sort(arr, n, j, key):
    if j < 0:
        return j
    
    if key < arr[j]:
        arr[j+1] = arr[j] 
        return sort(arr, n, j-1, key)
    else:
        return j
    
def iteration(arr, n, i):
    if i > n-1:
        return
    key=arr[i]
    j=i-1
    new_idx = sort(arr, n, j, key)
    arr[new_idx + 1] = key
    iteration(arr, n, i+1)

iteration(arr, n, 1)
print(arr)
