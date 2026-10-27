#Using 2 loops (Brute Force)
# TC = O(n^2)
# SC = O(1)

arr = [2,4,3,5,7,8,1]
target = 9

# Algorithm:
# 1. Choose each element with the outer loop.
# 2. Compare it with every element after it using the inner loop.
# 3. Print the pair if its sum equals target.
#
# Dry run:
# i = 0 (2): compare with 4, 3, 5, 7, 8, 1; 2 + 7 = 9 -> print 2, 7
# i = 1 (4): compare with 3, 5, 7, 8, 1; 4 + 5 = 9 -> print 4, 5
# i = 2 (3): no later value makes 9
# i = 3 (5): no later value makes 9
# i = 4 (7): no later value makes 9
# i = 5 (8): 8 + 1 = 9 -> print 8, 1
# i = 6 (1): no elements remain to compare
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i],arr[j])


# Using set(optimized)
# TC = O(n)
# SC = O(n)

seen = set()

# Algorithm:
# 1. For each number, calculate the complement needed to reach target.
# 2. If the complement is already in seen, print the pair.
# 3. Add the current number to seen for later lookups.
#
# Dry run:
# num = 2: complement 7 is not seen; add 2
# num = 4: complement 5 is not seen; add 4
# num = 3: complement 6 is not seen; add 3
# num = 5: complement 4 is seen -> print 4, 5; add 5
# num = 7: complement 2 is seen -> print 2, 7; add 7
# num = 8: complement 1 is not seen; add 8
# num = 1: complement 8 is seen -> print 8, 1
for num in arr:
    complement = target - num

    if complement in seen:
        print(complement, num)
    seen.add(num)

#Using Sorting and 2 pointers
# TC = O(nlogn)
# SC = O(1)

arr.sort()

left = 0
right = len(arr)-1

# Algorithm:
# 1. Sort the array, then place pointers at its first and last elements.
# 2. If their sum is target, print the pair and move both pointers inward.
# 3. If the sum is too small, move the left pointer right to increase it.
# 4. If the sum is too large, move the right pointer left to decrease it.
# 5. Stop when the pointers meet.
#
# Dry run after sorting: [1, 2, 3, 4, 5, 7, 8]
# 1 + 8 = 9 -> print 1, 8; move both pointers inward
# 2 + 7 = 9 -> print 2, 7; move both pointers inward
# 3 + 5 = 8 -> too small; move left to 4
# 4 + 5 = 9 -> print 4, 5; move both pointers inward
# The pointers meet, so the search ends.
while left < right:
    total = arr[left] +arr[right]

    if total == target:
        print(arr[left],arr[right])
        left += 1
        right -= 1
    elif total < target:
        left +=1
    else:
        right -= 1