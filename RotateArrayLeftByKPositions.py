#Using Slicing
#TC = O(n)
#SC = O(n)

arr = [1,2,3,4,5]
k = 2
k = k % len(arr)

rotated  = arr[k:] + arr[:k]
print("Rotated array: ",rotated)

# arr[k: ]--> [3,4,5]
# arr[ : k] -->[1,2]
# k % len(arr) handles cases where k is greater than array length

# Using a loop
# TC = O(nk)
# SC = O(1)
for i in range(k):
    first = arr[0]

    for j in range(len(arr)-1):
        arr[j]= arr[j+1]

    arr[-1]=first
print("Rotated array: ", arr)

# Dry run for arr = [1, 2, 3, 4, 5] and k = 2:
# i = 0: save 1; j shifts the remaining values left; put 1 at the end
#        [1, 2, 3, 4, 5] -> [2, 3, 4, 5, 1]
# i = 1: save 2; shift left again; put 2 at the end
#        [2, 3, 4, 5, 1] -> [3, 4, 5, 1, 2]
# The outer loop repeats k times, so the array is rotated left by 2.


#Using Reversal Algorithm(Efficient)
#TC= O(n)
#SC = O(1)
#
# Algorithm:
# 1. Reduce k modulo the array length.
# 2. Reverse the first k elements.
# 3. Reverse the remaining elements.
# 4. Reverse the entire array to complete the left rotation.

def reverse(array,start,end):
    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1

array = [1,2,3,4,5]
k = 2

n = len(array)
k = k % n

reverse(array,0,k-1)
reverse(array,k,n-1)
reverse(array,0,n-1)

# Dry run for array = [1, 2, 3, 4, 5] and k = 2:
# Reverse indexes 0..1: [2, 1, 3, 4, 5]
# Reverse indexes 2..4: [2, 1, 5, 4, 3]
# Reverse indexes 0..4: [3, 4, 5, 1, 2]
print("Rotaed array : ", array)