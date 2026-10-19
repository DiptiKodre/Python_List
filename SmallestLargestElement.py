nums = [23, 45, 67, 89, 12, 34, 56, 78, 90]

# smallest = nums[0]
# largest = nums[0]

# for i in range(len(nums)):
#     if nums[i]<smallest:
#         smallest = nums[i]
#     elif nums[i]>largest:
#         largest = nums[i]

# print("Smallest number is : ", smallest)
# print("Largest number is : ", largest)



# #using built-in functions

# print("Smallest element is : ", min(nums))
# print("Largest element is : ", max(nums))


#using sort function

nums.sort()
print("Smallest element is : ", nums[0])
print("Largest element is : ", nums[-1])
