# Maintain order
#in place change

nums = [1,0,2,4,3,0,0,3,5,1]
n = len(nums)

#TC = O(N)
#SC = O(N)
# temp = []
# for i in range(0,n):
#     if nums[i]!=0:
#         temp.append(nums[i])
# temp_len = len(temp)
# for i in range(0,temp_len):
#     nums[i] = temp[i]
# for i in range(temp_len,n):
#     nums[i] = 0
# print("Array after moving zeroes to end is:",nums)


#Optimal Solution
if len(nums) == 1:
    print("Array after moving zeroes to end is:",nums)
i = 0
while i<len(nums):
    if nums[i] == 0:
        break
    i+=1
if i == len(nums):
    print("Array after moving zeroes to end is:",nums)
j = i+1
while j<len(nums):
    if nums[j]!=0:
        nums[i],nums[j] = nums[j],nums[i]
        i+=1
    j+=1

print("Array after moving zeroes to end is:",nums)

#TC = O(n)
#SC = O(1)
