# Lists
"""
names = ['John','Bob', 'Mosh', 'Sara', 'Mary']

print(names)
print(names[:])
print(names[0]) #first element
print(names[-2]) #second from last
print(names[2:]) #from third element until the end
print(names[:2]) #first elements until second (last one don't count)
print(names[2:4]) #range of elements

names[0] = 'Vitor'# change value in a list
print(names)
"""

"""
#write a program to find the largest number in a list
numbers = [12,3,4,55,6,7,8,100,3,3,465,33]
largest = numbers[0]
for numb in numbers:
    if numb > largest:
        largest = numb
print(largest)
"""

# 2D Lists
"""
example: [
        1,2,3
        4,5,6
        7,8,9
        ]
"""
"""
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][2])
print(matrix)
matrix[0][1] = 20
print(matrix)

for row in matrix:
    for item in row:
        print(item)
        
"""
#List methods
"""
numbers = [5,2,1,5,7,4,7,8]
numbers.append(20) #insert at the end of the list
print(numbers)
numbers.insert(0,10) #insert in a specific index
print(numbers)
print('Remove the item 7 : ')
numbers.remove(7) #remove the first item that I want remove
print(numbers)
numbers.pop() #remove the last one
print(numbers)
print(numbers.index(5))#return the index
print(10 in numbers) #check if a number exist in the list
print(numbers.count(5)) # count the number of repetitions in a list
numbers.sort() #sort the list
print(numbers)
numbers.clear() #remove all values
print(numbers)

numbers2 = numbers.copy() #copy a list, at the end I have two separated lists

"""
#write a program to remove the duplicates in a list
numberCheck = [1,2,2,33,4,4,5,6,7,1,2,8,9,44,2,54,4,4,55,47,6]
numberCheck.sort()
print(numberCheck)
uniques = []

for number in numberCheck:
    if number not in uniques:
        uniques.append(number)
print(uniques)
