nums = [12,34,56,-45,67,99,3,24,36]

n = len(nums)

largest = nums[0]
# largest = float('-inf')
for i in range(0,n):
    if (nums[i]>largest):
        largest = nums[i]
print("Largest element in the array is : ",largest)


# TC = O(n)
# SC = O(1)