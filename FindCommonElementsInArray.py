#using set --> optimized approach
#TC = O(n+m) where n and m are the lengths of arr1 and arr2 respectively
#SC = O(min(n,m)) where n and m are the lengths of arr1 and arr2 respectively 
arr1 = [1,2,3,4,5]
arr2 = [4,5,6,7,8]

common = list(set(arr1) & set(arr2))
print("Common elements:", common)

#without using set 
#TC = O(n*m) where n and m are the lengths of arr1 and arr2 respectively
#SC = O(k) where k is the number of common elements
common_elements = []
for num in arr1:
    if num in arr2:
        common_elements.append(num)
print("Common elements:", common_elements)
