num = [2,4,6,8,10,12,14,16,18,20]

left = 0
right = len(num)-1

while left < right:
    num[left],num[right]= num[right],num[left] #swapping
    left+=1
    right-=1
print(num)