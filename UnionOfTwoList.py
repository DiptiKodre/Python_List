num1 = [1,2,3,4,5]
num2 = [4,5,6,7,8]

#using set union
union_set = list(set(num1).union(set(num2)))
print(union_set)

#USING | operator
union_set_operator = list(set(num1) | set(num2))
print(union_set_operator)

#USING CONCATENATION 
res = num1 + num2
print(res)  #all elements from both lists are included, but duplicates are not removed



