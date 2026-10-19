arr = [12, 34, 56, 12, 78,23, 34, 56, 78, 90]
def containsDuplicate(arr):
    hashset = set()

    for i in arr:
        if i in hashset:
            return True     #Contsains duplicate
        hashset.add(i)
    return False            #Does not contain duplicate
print(containsDuplicate(arr))

#TC = O(n)  
#SC = O(n)
