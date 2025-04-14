''' 

Selection Sort Algorithm 9/4/25

https://takeuforward.org/sorting/selection-sort-algorithm/

Solution - We will run two loops one from i = 0 to n-2 and other from i+1 to n-1
We will find the minimum from in the j loop and replace with i after the inner loop has been executed, TC will be O(N^2), SC O(1)

as outer loop will run from 0 to n-2 and 
inner from: 1 to n-1, 2 to n-1, 3 to n-1, 4 to n-1,... i.e. n-1 times, n-2 times,...2, 1 times

'''

arr = [13,46,24,52,20,9]

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_ind = i               # initialising min_ind with i bcz we have to swap the minimum value from the inner loop with i.

        for j in range(i+1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j

        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    
    return arr


ans = selection_sort(arr)
print(ans)
