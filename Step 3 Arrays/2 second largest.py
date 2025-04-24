''' 
Find Second Smallest and Second Largest Element in an array 24/4/25

https://takeuforward.org/data-structure/find-second-smallest-and-second-largest-element-in-an-array/

'''

# Bruteforce Approach TC O(Nlogn + 2N), SC O(N) ----------------------------------------

''' 
This is a brute force way sorting and then running two loops and finding only for n > 2
'''

'''

# arr = [13,46,24,52,20,9]
arr = [10, 10, 10]

n = len(arr)

arr.sort()

i, j = 1, n-2       # if n > 2, else no point of 2nd max and min
sec_min_found, sec_max_found = False, False

while i < n:
    if arr[i] != arr[0]: 
        sec_min = arr[i]
        sec_min_found = True
        break
    i += 1
while j >= 0:
    if arr[j] != arr[n-1]: 
        sec_max = arr[j]
        sec_max_found = True
        break
    j -= 1

if not sec_min_found:        # return -1 if not found second min and max
    sec_min = -1
if not sec_max_found:
    sec_max = -1

print(sec_min, sec_max)

'''

# Better Approach TC O(2N), SC O(1) ----------------------------------------


'''

arr = [13,46,24,52,20,9]
n = len(arr)

first_max, first_min = arr[0], arr[0]     # max and min element will be from the arr so initializing with arr[0] 

sec_max = float('-inf')  # Smallest possible number
sec_min = float('inf')   # Largest possible number

for i in range(1, n):
    if arr[i] > first_max:
        first_max = arr[i]
    if arr[i] < first_min:
        first_min = arr[i]

for i in range(0, n):
    if arr[i] > sec_max and arr[i] != first_max:
        sec_max = arr[i]
    if arr[i] < sec_min and arr[i] != first_min:
        sec_min = arr[i]

print(sec_min, sec_max)

'''

# Optimized Approach TC O(N), SC O(1) One pass


# arr = [13,46,24,52,20,9]
# arr = [4, 4, 9]
arr = [1, 5, 5, 4] 
# arr = [1, 1]
n = len(arr)

if n < 2:
    print("Number of elements in array is less than two", -1, -1)
else:
    first_max, sec_max = float('-inf'), float('-inf')
    first_min, sec_min = float('inf'), float('inf') 

    for i in range(0, n):
        if arr[i] > first_max:
            sec_max = first_max
            first_max = arr[i]
        elif  first_max > arr[i] > sec_max:    # same min elif logic for max too, arr = [1, 5, 5, 4] 
            sec_max = arr[i]


        if arr[i] < first_min:        # this fails for 4,9 as it will take first min as 4 but 9 < 4 so it will not go inside but 9 is the second min so adding one more elif in this 
            sec_min = first_min
            first_min = arr[i]
        elif first_min < arr[i] < sec_min:    # if arr[i] >= first_min it will go here 
            sec_min = arr[i]


    if sec_max == float('-inf'):     # simply check if they are not equal to inf 
        sec_max = -1
    if sec_min == float('inf'):
        sec_min = -1

    print(sec_min, sec_max)

