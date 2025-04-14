''' 

Insertion Sort Algorithm 9/4/25

https://takeuforward.org/data-structure/insertion-sort-algorithm/

Solution - We will run two loops one from 1 to <= n-1 as the first element will be sorted only and other from j=i-1 till >= 0
We will place the ith element at the correct position

the outer loop runs from 1 till <=n-1 i.e. n times
the inner loop 
1 time, 2 times,......., (n-1) times

TC O(N^2), SC O(1)
'''

arr = [13,46,24,52,20,9]

# ----------- This is not correct as we are not inserting it is swapping so it is not what needed although it passed.

# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1, n):
#         for j in range(i, 0, -1):
#             if arr[j-1] > arr[j]:
#                 arr[j-1], arr[j] = arr[j], arr[j-1]
#     return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key, j = arr[i], i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]        # moving the value at jth index to position 1 index ahead so that a space is created to adjust key 
            j-=1         # either j becomes -1 or where the element is < key
        arr[j+1] = key      # the last value of j which is either 0 if we check till the 1st element or the 
    return arr

ans = insertion_sort(arr)
print(ans)
