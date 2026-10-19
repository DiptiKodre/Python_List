num1 = [1,1,1,2,4,5,6,7,8,9]
num2 = [1,2,3,4,5,6,7,8,9]

n = len(num1)
m = len(num2)
result = []
i = 0
j = 0

while i<n and j<m:
    if num1[i]<num2[j]:
        if len(result) == 0 or result[-1] != num1[i]:
            result.append(num1[i])
        i+=1
    else:
        if len(result) == 0 or result[-1] != num2[j]:
            result.append(num2[j])
        j+=1

while i<n:
    if len(result) == 0 or result[-1] != num1[i]:
        result.append(num1[i])
    i+=1    

while j<m:
    if len(result) == 0 or result[-1] != num2[j]:
        result.append(num2[j])
    j+=1

print("Merged array is:",result)

#TC = O(n+m)
#SC = O(n+m)
       