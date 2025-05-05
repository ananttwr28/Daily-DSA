''' 
rotate the array left/right by k place 28/4/25

https://takeuforward.org/data-structure/

'''

# Right Rotate by d Places

arr = [1, 2, 3, 4, 5]
n = len(arr)
d = 2
new_list = []

d = d%n         # if n is 5 and d is 7 then after 5 rotations the arr will be back to org and it will be rotated 2 steps more, if left d as normal 5-7 will give -ve value which is wrong


for i in range(n-d, n):
    new_list.append(arr[i])
for i in range(n-d-1, -1, -1):
    arr[i+d] = arr[i]
for i in range(0, len(new_list)):
    arr[i] = new_list[i]

print(arr)