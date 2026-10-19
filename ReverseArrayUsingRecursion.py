#TC = O(n)
#SC = O(n)

num = [2,4,6,8,10,12,14,16,18,20]

def reverse_array(arr, left, right):
    if left >= right:
        return # stopping condition
    arr[left],arr[right]= arr[right],arr[left] #swapping
    reverse_array(arr,left+1,right-1) #recursive call

reverse_array(num,0,len(num)-1)
print(num)

reverse_array(num,2,7)
print(num)