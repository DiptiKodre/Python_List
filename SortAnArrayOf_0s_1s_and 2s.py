# approach 1 --> using sort()
# TC = O(nlogn)
# SC = O(1)

arr = [2,0,1,2,1,0,1,2,0]
arr.sort()
print(arr)

# approach 2--> counting 0s , 1s ans 2s
# TC = O(n)
# SC = O(1)

# Algorithm:
# 1. Count how many 0s, 1s, and 2s are present.
# 2. Rewrite the array in order: all 0s, then all 1s, then all 2s.
# 3. Return the sorted array.

def sort012(arr):
    count0 = 0
    count1 = 0
    count2 = 0

    # count 0s, 1s ans 2s
    for num in arr:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1

    # Replace elements
    index = 0

    for i in range(count0):
        arr[index] = 0
        index += 1

    for i in range(count1):
        arr[index] = 1
        index += 1

    for i in range(count2):
        arr[index] = 2
        index += 1

    return arr
print(sort012(arr))

# Dry run for arr = [2, 0, 1, 2, 1, 0, 1, 2, 0]:
# Counts: count0 = 3, count1 = 3, count2 = 3
# Fill 0s -> [0, 0, 0, 2, 1, 2, 1, 2, 1]
# Fill 1s -> [0, 0, 0, 1, 1, 1, 2, 2, 2]
# Fill 2s -> [0, 0, 0, 1, 1, 1, 2, 2, 2]
# Final sorted array: [0, 0, 0, 1, 1, 1, 2, 2, 2]

# Approach 3 --> Dutch National Flag Algorithm (Three pointers)
# TC = O(n)
# SC = O(1)

#Algorithm:
# 1. Keep three ranges:
#    - [0 : low-1] -> all 0s
#    - [low : mid-1] -> all 1s
#    - [high+1 : end] -> all 2s
# 2. Traverse with 'mid' from left to right.
# 3. If arr[mid] == 0, swap with arr[low] and move low and mid forward.
# 4. If arr[mid] == 1, move mid forward.
# 5. If arr[mid] == 2, swap with arr[high] and move high backward.
# 6. Stop when mid > high.

# 3 pointers:
# low : position 0
# mid : current element
# high : position 2

# Rules:
# 1) if arr[mid] == 0 --> swap arr[low] and arr[mid], increment both low and mid
# 2) if arr[mid] == 1 --> increment mid
# 3) if arr[mid] == 2 --> swap arr[mid] arr [high], decrement high

def sort_012_DNF(arr):
    low = 0
    mid = 0
    high = len(arr) -1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif arr[mid] ==1:
            mid += 1

        else:
            arr[mid], arr[high] = arr[high],arr[mid]
            high -= 1

    return arr
print(sort_012_DNF(arr))

# Dry run for arr = [2, 0, 1, 2, 1, 0, 1, 2, 0]:
# Start: low = 0, mid = 0, high = 8
# arr[0] = 2 -> swap with arr[8] => [0, 0, 1, 2, 1, 0, 1, 2, 2], high = 7
# arr[0] = 0 -> swap with arr[0] => no change, low = 1, mid = 1
# arr[1] = 0 -> swap with arr[1] => no change, low = 2, mid = 2
# arr[2] = 1 -> mid = 3
# arr[3] = 2 -> swap with arr[7] => [0, 0, 1, 2, 1, 0, 1, 2, 2], high = 6
# arr[3] = 2 -> swap with arr[6] => [0, 0, 1, 1, 1, 0, 2, 2, 2], high = 5
# arr[3] = 1 -> mid = 4
# arr[4] = 1 -> mid = 5
# arr[5] = 0 -> swap with arr[2] => [0, 0, 0, 1, 1, 1, 2, 2, 2], low = 3, mid = 6
# stop because mid > high
# Final array: [0, 0, 0, 1, 1, 1, 2, 2, 2]