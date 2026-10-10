nums = [12, 8, 34, 56, 78, 90]

# rev_list = nums.reverse()
# print("The reverse of the list is : ", nums)


# # using slicing method

# rev_list = nums[::-1]
# print("The reverse of the list is : ", rev_list)


# #using for loop

# rev_list = []
# for i in range(len(nums)-1, -1, -1):
#     rev_list.append(nums[i])

# print("The reverse of the list is : ", rev_list)


##using while loop

# rev_list = []
# i = len(nums)-1
# while i >= 0:
#     rev_list.append(nums[i])
#     i -= 1

# print("The reverse of the list is : ", rev_list)

#using built-in function reversed()

rev_list = list(reversed(nums))
print("The reverse list is : " , rev_list)

