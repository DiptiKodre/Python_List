#TC = O(n)
#SC = O(1)
arr = [5,2,8,1,3,1]

smallest = float("inf")
second_smallest = float("inf")

for num in arr:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Smallest element : ", smallest)
print("Second smallest element : ",second_smallest)