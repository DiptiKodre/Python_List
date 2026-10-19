# Brute force  approach
#TC = O(n^2)
#SC  =O(k) where k is the number of duplicate elements

arr = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 1]
duplicates = []

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])

print("Duplicate elements:", duplicates)


#Optimal approach using set
#TC = O(n)
#SC = O(n)

seen = set()
duplicates = set()

for num in arr:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicate elements:", list(duplicates))