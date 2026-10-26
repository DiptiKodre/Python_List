# Using dictionary

# TC = O(n)
# SC = O(k)
arr = [1,2,2,3,1,4,2]


freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)


#Using get()

frequency= {}
for num in arr:
    frequency[num] = freq.get(num,0) + 1
print(frequency)


#Without a dictionary
# TC = O(n^2)
# SC = O(k))
visited =[]
for num in arr:
    if num not in visited:
        count = 0

        for x in arr:
            if x == num:
                count += 1
        print(num, ":", count)
        visited.append(num)

#Using count()
# TC = O(n*k)....n : number of elements   k: number of distinct elements
# SC = O(k)

for num in set(arr):  #set removes duplicates

    print(num, ":",arr.count(num))