list = [12,23,34,45,56,67,78,89,90]

print("The original list is : ", list)

##using temporary variable
# temp = list[0]
# list[0] = list[-1]
# list[-1] = temp
# print("The list after interchanging the first and last elements is : ", list)

##using direct assignment
# list[0], list[-1] = list[-1], list[0]
# print("The list after interchanging the first and last elements is : ", list)

# #using tuple variable
# pair = list[0], list[-1]
# list[-1], list[0] = pair
# print("The list after interchanging the first and last elements is : ", list)

# #using * operator
# a , *mid, b = list
# list = [b, *mid,a]
# print("The list after interchanging the first and last elements is : ", list)

# using slicing method
list = list[-1:]+list[1:-1]+list[:1] #90 +[23,34,45,56,67,78,89] + [12]
print("The list after interchanging the first and last elements is : ", list)