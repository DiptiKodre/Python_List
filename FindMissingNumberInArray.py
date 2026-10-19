nums = [ 9,6,4,2,3,5,7,0,1]

n = len(nums)

#Brute force solution
#TC = O(n^2)
#SC = O(1)
# for i in range(0,n+1):
#     if i not in nums:
#         print("Missing number in the array is:",i)
#         break


#dictionary based solution
#TC = O(n)
#SC = O(n)

# freq = {}
# for i in range(0,n+1):
#     freq[i] = 0
# for num in nums:
#     freq[num] = 1
# for k,v in freq.items():
#     if v == 0:
#         print("Missing number in the array is:",k)


# Optimal solution
# TC = O(n)
# SC = O(1)

total_sum = sum(nums)
expsum = n*(n+1)//2
missng_number = expsum - total_sum
print("Missing number in the array is:",missng_number)
