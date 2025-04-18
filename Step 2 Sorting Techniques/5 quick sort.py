''' 

Merge Sort Algorithm 13/4/25

https://takeuforward.org/data-structure/quick-sort-algorithm/

Dry run in notes

Avg and Best case -> TC O(NLogn), SC O(1)+O(logN) (Recursion stack space)
Worst case (when pivot is smallest/largest leading to unbalanced div)-> TC O(N^2), SC O(1)+O(N) (Recursion stack space)
'''

# arr = [13,46,24,52,20,9]
arr = [4,6,2,5,7,9,1,3]
n = len(arr)

def partition_idx(arr, low, high):
    pivot = arr[low]
    i = low
    j = high

    while i < j:
        while arr[i] <= pivot and i <= high:
            if i == high:
                break
            i += 1
        while arr[j] > pivot and j >= low:
            if j == low:
                break
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr, low, high):
    if low < high:
        p_idx = partition_idx(arr, low, high)
        
        quick_sort(arr, low, p_idx-1)
        quick_sort(arr, p_idx+1, high)

quick_sort(arr, 0, n-1)
print(arr)

