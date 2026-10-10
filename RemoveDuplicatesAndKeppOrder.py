# TC = O(n^2)
# SC = O(n)

nums = [1,23,2,4,2,5,6,7,8,9,1,2,3,4,5]

newList = []

for ele in nums:
    if ele not in newList:
        newList.append(ele)

print("The list after removing duplicates is : ", newList)


# #using dict.fromkeys() method

# newList = list(dict.fromkeys(nums))
# print("The list after removing duplicates is : ", newList)


# #using set() method

# newList = list(set(nums))
# print("The list after removing duplicates is : ", newList)


# #using collections.OrderedDict() method

# from collections import OrderedDict
# newList = list(OrderedDict.fromkeys(nums))
# print("The list after removing duplicates is : ", newList)