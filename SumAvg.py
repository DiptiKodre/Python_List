nums = [12,56,34,89,90,78,23,45]

# sum = 0
# for val in nums:
#     sum += val

# print("The sum of the list is : ", sum)

# avg = sum/len(nums)
# print("The average of the list is : ", avg)


# #using built-in functions
# sum = sum(nums)
# avg = sum/len(nums)
# print("The sum of the list is : ", sum)
# print("The average of the list is : ", avg)


sum = 0
len = 0
for val in nums:
    sum += val
    len += 1

print("The sum of the list is : ", sum)

avg = sum/len
print("The average of the list is : ", avg)