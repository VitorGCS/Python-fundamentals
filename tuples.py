#TUPLES
#Tuples are imutable objects!

numbersList = [1,2,3]
numberTuples = (1,2,3)
#numberTuples[0] = 10  #TypeError: 'tuple' object does not support item assignment
print(numberTuples[0])

#Unpacking - note: also can be used in List
coordinates = (1,2,3)

#coordinates[0]*coordinates[1]* coordinates[2]
"""
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x * y * z
"""
x,y,z = coordinates #unpacking
print(x)
print(y)
print(z)

