def print_list(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx], end =" ")
    print_list(list,idx+1)

fruits = ['apple','banana','cherry','date']
print_list(fruits)
