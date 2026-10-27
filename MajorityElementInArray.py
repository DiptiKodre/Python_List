# The majority element in an array is an element which 
# appears more than n/2 times

#using dictinary
# TC = O(n)
# SC = O(n)

arr = [2,2,1,2,3,2,2]

freq = {}

for num in arr:
    freq[num] = freq.get(num,0)+1
for num, count in freq.items():
    if count > len(arr)//2:
        print("Majority element: ",num)
        break
    print("No majority element")

# using count()
# TC = O(n^2)
# SC = O(1)

for num in arr:
    if arr.count(num) > len(arr)//2:
        print("Majority element : ",num)
        break
    else:
        print("No majority element")

# Boyer- Moore Voting algorithm(Imp)--> Optimal solution
# TC = O(n)
# SC = O(1)
# Algorithm:
# 1. When count is 0, choose the current number as the candidate.
# 2. Increment count when the current number matches the candidate; otherwise decrement it.
# 3. Count the candidate in the array to confirm it appears more than n/2 times.
#
# Dry run for arr = [2, 2, 1, 2, 3, 2, 2]:
# num:       2  2  1  2  3  2  2
# candidate: 2  2  2  2  2  2  2
# count:     1  2  1  2  1  2  3
# Candidate 2 appears 6 times, which is more than 7 // 2, so it is the majority element.
candidate = 0
count = 0

for num  in arr:
    if count == 0:
        candidate = num
    if num == candidate:
        count += 1
    else:
        count -= 1

# verify the candidate

if arr.count(candidate) > len(arr)//2:
    print("Majority element: ", candidate)
else:
    print("No majority element")
