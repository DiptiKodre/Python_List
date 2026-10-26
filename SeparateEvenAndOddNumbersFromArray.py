arr = [1,2,3,4,5,6,7,8,9]

#Using for loop
#TC = O(n)
#SC = O(n)
even =[]
odd = []

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers : ",even)
print("Odd numbers : ",odd)

# Using list Comprehension

even_nums = [x for x in arr if x%2 == 0]
odd_nums = [x for x in arr if x%2 != 0]
print("Even: ", even_nums)
print("Odd: ",odd_nums)

#Using a Function

def separate_even_odd(array):
    evennums =[]
    oddnums = []

    for x in arr:
        if x%2 == 0:
            evennums.append(x)
        else:
            oddnums.append(x)
    return even,odd

array = [1,2,3,4,5,6,7,8,9]
evennums, oddnums = separate_even_odd(array)
print("Even: ", evennums)
print("Odd : ", oddnums)