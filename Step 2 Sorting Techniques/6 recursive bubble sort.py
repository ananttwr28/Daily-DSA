''' 
Recursive Bubble Sort Algorithm 20/4/25
https://takeuforward.org/arrays/recursive-bubble-sort-algorithm/

O(N^2) TC and O(N) SC for max fn at once in call stack
'''

arr = [52, 42, 1, 24, 3]
n = len(arr) 

def sort(arr, n, i, j=0):
    if j > n-2-i:
        return
    
    if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j] 
    sort(arr, n, i, j+1)
    
def iteration(arr, n, i):
    if i > n-2:
        return
    sort(arr, n, i)
    iteration(arr, n, i+1)

iteration(arr, n, 0)
print(arr)
