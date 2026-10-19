#TC = O(n)
#SC = O(n)

arr = [12,34,21,45,56,67,64.67]

def containsDuplicate(arr):
        hashset = set()
        for i in arr:
                if i in hashset:   #If the value already exists, a duplicate was found, so the function returns True.
                        return True
                hashset.add(i)  #Adds the current value to the set if it has not already been found.
        return False

print(containsDuplicate(arr))
   
