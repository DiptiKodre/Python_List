nums = [5,-2,3,9,0,6,10,7]
n = len(nums)
#method 1 = slicing
#nums[:] = [nums[-1]]+ nums[0:n-1]
# nums[:] = nums[n-1:] + nums[0:n-1]
# print("Array after right rotation by one place is:",nums)

#method 2
temp = nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1]= nums[i]
nums[0] = temp
print("Array after right rotation by one place is:",nums)

#TC = O(n)
#SC = O(1)