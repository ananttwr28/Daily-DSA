''' 

Bubble Sort Algorithm 9/4/25

https://takeuforward.org/data-structure/bubble-sort-algorithm/

Solution - We will run two loops one from 0 to < n-1 i.e. 4 times for n = 5 as the first element will be sorted only and other from i=0 to <=n-2-i
We will find the max b/w i and i+1 th element and swap by this the max element will reach at last position.

as outer loop will run from 0 to n-2 i.e. N times
inner from: 0 to n-2, 0 to n-3, 0 to 1, ... i.e. n-1 times, n-2 times,...2, 1 times

TC O(N^2), SC O(1)
'''

arr = [13,46,24,52,20,9]

def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        swapped = 0       # moved it here instead of before i loop coz it should be take fresh 0 value after each ith iteration else it would have been set bcz of previous iterations and will check again
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = 1        # if after 1st iteration of i, no swap took place means all the elements are in sorted order, since no element was greater than the one after it.
        if swapped == 0:
            break    # break out of the outer loop, so only 1 iteration of i loop will be made hence the TC will be O(1)*O(N) 
    return arr


ans = bubble_sort(arr)
print(ans)
