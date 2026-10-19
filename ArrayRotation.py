n = int(input("enter size of array: "))
arr = list(map(int, input("Enter element separated by space : ")))

d = int(input("Enter number of rotations : "))

for i in range(d):
    temp = arr[0]
    for j in range(n-1):
        arr[j] = arr[j+1]
        arr[n-1] = temp