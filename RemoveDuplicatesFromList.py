fruits = ["apple", "banana", "orange", "apple", "kiwi", "banana", "grape"]

#TC = O(n^2) --> because of the nested loop
def remove_duplicates(fruits):
    unique_fruits = []
    for fruit in fruits:
         if fruit not in unique_fruits:
                unique_fruits.append(fruit)
    return unique_fruits

print(remove_duplicates(fruits))


#TC = O(n) --> because of the dictionary
#using dictionary keys to remove duplicates
def remove_duplicates_using_dict(fruits):
    return list(dict.fromkeys(fruits))

print(remove_duplicates_using_dict(fruits))

#TC = O(n) --> because of the set
#using set to remove duplicates-->unordered collection of unique elements
def remove_duplicates_using_set(fruits):
    return list(set(fruits))

print(remove_duplicates_using_set(fruits))