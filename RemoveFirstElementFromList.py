num = [1, 2, 3, 4, 5]

num.pop(0)
print(num)

#using slicing
num = num[1:]
print(num)

#using delete keyword
del num[0]
print(num)

#using collections.deque
from collections import deque

num = deque([1, 2, 3, 4, 5])
num.popleft()
print(list(num))