
#TC = O(n) where n is the length of arr
#SC = O(1) since we are using only two variables to store the smallest and second smallest numbers
arr = [5,2,8,1,3,1,4,6,7,0]


smallest = float('inf')
second_smallest = float('inf')

for num in arr:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num <second_smallest and num != smallest:
        second_smallest = num
print("Smallest number:", smallest)
print("Second smallest number:", second_smallest)



#####################################################333
#TC = O(nlogn) where n is the length of arr
#SC = O(n) since we are creating a new list to store unique elements
unique = list(set(arr))
unique.sort()

print("Smallest number:", unique[0])
print("Second smallest number:", unique[1])
