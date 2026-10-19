nums = [1,23,45,67,78,89,90,100]

n = len(nums)

for i in range(0,n-1):
    if nums[i]>nums[i+1]:
        print("Array is not sorted")
        break
else:
    print("Array is sorted")