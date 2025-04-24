''' 

Check if an Array is Sorted 24/4/25

https://takeuforward.org/data-structure/check-if-an-array-is-sorted/

'''
# BruteForce Approach  ------------------------------------

# Two loop O(2*N^2) checking for each element if it is greater or smaller than rest

'''

arr = [5, 4, 7]
n = len(arr)

if n <= 1:
    print("Array is sorted")

else:
    def is_sorted_increasing(arr, n):
        is_sorted = True
        for i in range(0, n-1):
            for j in range(i+1, n):
                if arr[i] > arr[j]:
                    is_sorted = False
                if not is_sorted: # break early
                    break
            if not is_sorted: # break early
                    break
        return is_sorted

    def is_sorted_decreasing(arr, n):
        is_sorted = True
        for i in range(0, n-1):
            for j in range(i+1, n):
                if arr[i] < arr[j]:
                    is_sorted = False
                if not is_sorted: # break early
                    break
            if not is_sorted: # break early
                    break
        return is_sorted

    sorted_inc = is_sorted_increasing(arr, n)
    sorted_dec = is_sorted_decreasing(arr, n)

    if sorted_inc or sorted_dec:
        print("Array is sorted")
    else:
        print("Array is unsorted")
'''

# Optimised Approach  ------------------------------------

# This is the optimised approach O(2n) for checking both increasing and decreasing order

'''

arr = [5, 4, 2]
n = len(arr)

def is_sorted_increasing(arr, n):
    is_sorted = True
    for i in range(1, n):
        if arr[i-1] > arr[i]:
            is_sorted = False
        if not is_sorted: # break early
            break
    return is_sorted

def is_sorted_decreasing(arr, n):
    is_sorted = True
    for i in range(1, n):
        if arr[i-1] < arr[i]:
            is_sorted = False
        if not is_sorted: # break early
            break
    return is_sorted

sorted_inc = is_sorted_increasing(arr, n)
sorted_dec = is_sorted_decreasing(arr, n)

if sorted_inc or sorted_dec:
    print("Array is sorted")
else:
    print("Array is unsorted")

'''


# Optimised Approach Clean Code One Pass ------------------------------------

# TC O(n)

arr = [5, 4, 2]
n = len(arr)

def is_sorted_either_way(arr, n):
    is_sorted_inc = 0
    is_sorted_dec = 0

    for i in range(1, n):
        if arr[i-1] < arr[i]:         # if the elements are in inc order this keeps on increasing
            is_sorted_inc += 1
        if arr[i-1] > arr[i]:         # if the elements are in dec order this keeps on increasing
            is_sorted_dec += 1
    if is_sorted_inc == 0 or is_sorted_dec == 0:         # 3,4,5,3,2 both cases happen and both have non zero value means arr is unsorted, one has to be zero
        return True
    return False

is_sorted = is_sorted_either_way(arr, n)

if is_sorted:
    print("Array is sorted")
else:
    print("Array is unsorted")