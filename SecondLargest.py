# TC = O(n)
#SC = O(1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

secondLargest = arr[0]
largest = arr[0]

for  i in range(len(arr)):
    if arr[i]> largest:
        secondLargest = largest
        largest = arr[i]
    elif arr[i] > secondLargest and arr[i] != largest:
        secondLargest = arr[i]

print("The second largest element in the list is : ", secondLargest)