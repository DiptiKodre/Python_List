# using set--> fastest for unique elements
# TC = O(n+m)
# SC = O(n+m)
arr1 = [1,2,3,4,5]
arr2 = [3,4,5,6,7]

result =list(set(arr1)& set(arr2))
print("Intersection : ",result)

# Using loop(without set)
# TC = O(n+m)
# SC = O(k)...k--> number of common unique elements
result = []
for num in arr1:
    if num in arr2 and num not in result:
        result.append(num)
print("Intersection: ",result)


# Using list comprehension

# TC = O(n*m)
# SC = O(k)...k--> number of matching elements (O(n) in the worst case)
common = [num for num in arr1 if num in arr2]
print(common)