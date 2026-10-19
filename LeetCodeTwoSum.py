#Constraints --> use element only once
        # only one solution exists
#return index of elements

nums = [5,9,1,2,4,15,6,3]
target = 13
n = len(nums)
#brute Force 
#TC = O(n^2)
#SC = O(1)

for i in range(0,n-1):
    for j in range(i+1,n):
        if nums[i] +  nums[j] == target:
            print([i,j])

# using hashmap--> optimal solution
#TC = O(n)
#SC = O(n)
def twoSum(nums):
    hash_map = {}
    for i in range(0,n):
        remaining = target - nums[i]
        if remaining in hash_map:
            return[hash_map[remaining],i]
        hash_map[nums[i]] = i

print(twoSum(nums))
