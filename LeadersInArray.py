# A leader in an array is an element that is greater than or equal to
# every element on its right side
# The rightmost element  always a leader because there are no elements on its right
# Ex. arr = [16,17,4,3,5,2]
# Leaders : [17,5,2]

arr = [16,17,4,3,5,2]
n = len(arr)

# Brute forcr approach
# TC = O(n^2)
# SC = O(1)

for i in range(n):
    is_leader = True

    for j in range(i+1,n):
        if arr[i]<arr[j]:
            is_leader = False
            break

    if is_leader:
        print(arr[i], end=" ")

# Optimal solution
# TC = O(n)
# SC = O(n)
#
# Algorithm:
# 1. Start from the rightmost element; it is always a leader.
# 2. Scan the array from right to left, keeping the maximum seen so far.
# 3. If the current element is greater than or equal to that maximum, it is
#    a leader. Add it and update the maximum.
# 4. Reverse the collected leaders to restore their original array order.

max_right = arr[n-1]
leaders = [max_right]

for i in range(n-2,-1,-1):
    if arr[i]>= max_right:
        leaders.append(arr[i])
        max_right = arr[i]

leaders.reverse()

print("\nLeaders : " ,leaders)


# Dry run for arr = [16, 17, 4, 3, 5, 2]:
# Start: max_right = 2, leaders = [2]
# i = 4: arr[i] = 5 >= 2 -> max_right = 5, leaders = [2, 5]
# i = 3: arr[i] = 3 < 5 -> no change
# i = 2: arr[i] = 4 < 5 -> no change
# i = 1: arr[i] = 17 >= 5 -> max_right = 17, leaders = [2, 5, 17]
# i = 0: arr[i] = 16 < 17 -> no change
# Reverse leaders -> [17, 5, 2]
