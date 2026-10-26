#using + opeartor

#TC = O(n+m)
#SC = O(n+m)

arr1 = [1,2,3]
arr2 = [3,2,1]
merged = arr1 + arr2
print(merged)

# Using extend()
#TC = O(m)
#SC = O(m)

arr1.extend(arr2)
print(arr1)

#Using a for loop
#TC = O(n+m)
#SC = O(n+m)
array1 = [1,2,3]
array2 = [3,2,1]
merge = []
for i in array1:
    merge.append(i)

for i in array2:
    merge.append(i)

print(merge)