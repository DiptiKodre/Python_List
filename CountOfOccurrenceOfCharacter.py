list = ["g","a","b","c","d","e","g","a","b","c","d","e"]
# count = 0
# for ele in list:
#     if ele == "g":
#         count += 1
# print("The count of occurrence of character 'g' is : ", count)

#user input
n = int(input("Enter the number of elements in the list : "))
list = []
for i in range(0,n):
    ele = input("Enter the element : ")
    list.append(ele)

print("The list is : ", list)

find = input("Enter the character to find the occurrence : ")
count =0 
for ele in list:
    if ele == find:
        count += 1
print("The count of occurrence of character '", find, "' is : ", count)


# #using count() method
# total = list.count("g")
# print("The count of occurrence of character 'g' is : ", total)


# #using operator.countOf() method
# import operator
# total = operator.countOf(list, "g")
# print("The count of occurrence of character 'g' is : ", total)


# #using collections.Counter() method
# from collections import Counter
# total = Counter(list)
# print("The count of occurrence of character 'g' is : ", total["g"])
