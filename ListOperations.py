list =[1,3,4,7,5,6,8,9]
list.append(10)
print(list)

list.insert(2, 99)  # Insert 99 at index 2
print(list)

list.remove(7)  # Remove the first occurrence of 7
print(list)

list.pop() # Remove and return the last item
print(list)

list.pop(3) # Remove and return the item at index 3
print(list)

list.sort()  # Sort the list in ascending order
print(list)

list.sort(reverse=True)  # Sort the list in descending order
print(list)

list.reverse()  # Reverse the order of the list
print(list)

print(len(list))  # Get the number of items in the list

list.clear()  # Remove all items from the list
