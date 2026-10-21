nums = [5,9,1,2,4,15,6,3]
target = 13
n = len(nums)


# Brute Force Solution
# TC = O(n^2)
# SC = O(1)
# for i in range(0,n-1):
#     for j in range(i+1,n):
#         if nums[i]+nums[j]==target:
#             print("Pair found at index:",i,"and",j)
#             break


#Optimal Solution
# TC = O(n)
# SC = O(n)
def  twoSum(nums,target):
    hashmap = {}
    for i in range(0,n):
        remaining = target - nums[i]
        if remaining in hashmap:
            print("Pair found at index:",hashmap[remaining],"and",i)
            break
        hashmap[nums[i]] = i   
        # nums[0] = 5
        # hashmap[5] = 0     #stores the current number as a key in the dictionary and its index as the value.
# hashmap = {}
# for i in range(0,n):
#     remaining = target - nums[i]
#     if remaining in hashmap:
#         print("Pair found at index:",hashmap[remaining],"and",i)
#         break
#     hashmap[nums[i]] = i   
    # nums[0] = 5
    # hashmap[5] = 0     #stores the current number as a key in the dictionary and its index as the value.

# For example, when i = 0:
# nums[0] = 5
# hashmap[5] = 0     #stores the current number as a key in the dictionary and its index as the value.
#then dict becomes {5: 0}

