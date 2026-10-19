fruits1 = ["apple", "banana", "cherry", "date"]
fruits2 = ["banana", "cherry", "fig", "grape"]

#using list comprehension
common_fruits = [i for i in fruits1 if i in fruits2]
print(common_fruits)

#using set intersection
common_fruits_set = list(set(fruits1).intersection (set(fruits2)))
print(common_fruits_set)

#using for loop
common_fruits_loop = []
for i in fruits1:
    if i in fruits2:
        common_fruits_loop.append(i)
print(common_fruits_loop)   

#using  & operator
common_fruits_set_operator = list(set(fruits1) & set(fruits2))  
print(common_fruits_set_operator)

#using filter and lambda function
res = list(filter(lambda x : x in fruits2,fruits1))
print(res)

#using Counter from collections module
from collections import Counter
counter1 = Counter(fruits1) & Counter(fruits2)
common_fruits_counter = list(counter1.elements())   
print(common_fruits_counter)