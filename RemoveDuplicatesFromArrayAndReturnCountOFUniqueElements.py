nums = [ 1,1,1,2,3,4,4,7,9,9,9,10]
n = len(nums)

# freq_map = {}
# for i in range(0,n):
#     freq_map[nums[i]] = 0
# j = 0
# for k in freq_map:
#     nums[j] = k
#     j+=1
# print("Count of unique elements is:",j)

#Optimal Solution
if n == 1:
    print("Count of unique elements is:",1)
i=0
j=i+1
while j<n:
    if nums[j]!= nums[i]:
        i+=1
        nums[i],nums[j] = nums[j],nums[i]
    j+=1

print("Count of unique elements is:",i+1)