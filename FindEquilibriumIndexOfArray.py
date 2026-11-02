# Equilibrium Index:
# An index in an array where the sum of elements on the left side is equal
# to the sum of elements on the right side.
# Example: arr = [1, 3, 5, 2, 2] -> equilibrium index is 2 because
# left sum = 1 + 3 = 4 and right sum = 2 + 2 = 4.

# Approach 1 --> Using Two loops (Brute Force)
# TC = O(n^2)
# SC = O(1)

# Algorithm:
# 1. For each index i, compute the sum of elements on the left.
# 2. Compute the sum of elements on the right.
# 3. If both sums are equal, return i.

def equilibriumIndex(arr):
    n = len(arr)

    for i in range(n):
        left_sum = 0
        right_sum = 0

        # Calculate left sum
        for j in range(i):
            left_sum += arr[j]

         # Calculate right sum
        for j in range(i+1,n):
            right_sum += arr[j]

        if left_sum == right_sum:
            return i
    return -1

arr = [1,3,5,2,2]
print(equilibriumIndex(arr))

# Dry run for arr = [1, 3, 5, 2, 2]:
# i = 0: left = 0, right = 3 + 5 + 2 + 2 = 12 -> not equal
# i = 1: left = 1, right = 5 + 2 + 2 = 9 -> not equal
# i = 2: left = 1 + 3 = 4, right = 2 + 2 = 4 -> equal
# Return 2

# Using Total Sum (Optimized approach)
# TC = O(n)
# SC = O(1)
#
# Algorithm:
# 1. Compute total_sum of the array.
# 2. Maintain leftSum while scanning left to right.
# 3. At each index, rightSum = total_sum - leftSum - arr[i].
# 4. If leftSum == rightSum, return i.

def equilibrium_index(arr):
    total_sum = sum(arr)
    leftSum = 0
    for i in range(len(arr)):
        rightSum = total_sum - leftSum - arr[i]

        if leftSum == rightSum:
            return i

        leftSum += arr[i]

    return -1
print(equilibrium_index(arr))

# Dry run for arr = [1, 3, 5, 2, 2]:
# total_sum = 13
# i = 0: leftSum = 0, rightSum = 13 - 0 - 1 = 12 -> not equal
# i = 1: leftSum = 1, rightSum = 13 - 1 - 3 = 9 -> not equal
# i = 2: leftSum = 4, rightSum = 13 - 4 - 5 = 4 -> equal
# Return 2
