nums = [5,10,-3,-1,-10,6]

# //Brute force solution
# //TC = O(n+(n/2))
# //SC = O(n)

# positive = []
# negative = []

# for num in nums:
#     if num>=0:
#         positive.append(num)
#     else:
#         negative.append(num)

# for i in range(0,len(positive)):
#     nums[2*i] = positive[i]
#     nums[(2*i)+1] = negative[i]

# print(nums)


# Optimal Solution
#TC =O(N)
#SC = O(N)
n = len(nums)
result=[0]*n
pos_index = 0
neg_index = 1

for i in range(0,n):
    if nums[i]>=0:
        result[pos_index] = nums[i]
        pos_index+=2
    else:
        result[neg_index] = nums[i]
        neg_index+=2

print(result)
