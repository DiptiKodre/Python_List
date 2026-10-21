nums = [3,9,5,6,7,2]
k = 3

# #method 1 - brute force
# n = len(nums)
# rotations = k%n

# for _ in range(0, rotations):
#     element = nums.pop()
#     nums.insert(0,element)
# print("Array after right rotation by k places is:",nums)
# TC = O(n*k)
# SC = O(1)

# #method 2=  slicing
# n = len(nums)
# k = k%n

# nums[:]=nums[n-k:]+nums[0:n-k]
# print("Array after right rotation by k places is:",nums)

# TC = O(n)
# SC = O(1)

#method 3 - optimal solution
n = len(nums)
k = k%n
def reverse(nums, left, right):
    while left<right:
        nums[left],nums[right]= nums[right],nums[left]
        left += 1
        right -=1
reverse(nums,n-k,n-1)  # reverse last k elements
reverse(nums,0,n-k-1)   # reverse first n-k elements
reverse(nums,0,n-1)      # reverse whole array
print("Array after right rotation by k places is:",nums)


# TC = O(n)
# SC = O(1)
