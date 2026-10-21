num = [1, 2, 3, 4, 5]

#using list comprehension
#TC = O(n) --> because of the single loop
square = [x*x for x in num]
print(square)

#using for loop
#TC = O(n) --> because of the single loop
squares = []
for i in num:
    squares.append(i*i)
print(squares)

#using map function
#TC = O(n) --> because of the single loop
squares_map = list(map(lambda x: x*x, num))
print(squares_map)