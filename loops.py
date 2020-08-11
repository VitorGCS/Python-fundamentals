#while statement
"""
i = 1
while i <= 5:
    print('*'*i)
    i = i+1
print("Done")
"""
#Guessing Game: you have to gess the number from 1 to 10 and you have three attemts
"""
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit :
    gess = int(input('Guess: '))
    guess_count +=1
    if gess == secret_number:
        print('You won !')
        break
else:
    print('Sorry you failed')
# while loop can have an else clause, like if !!!!!
"""

#Car game
"""
command =''
started = False
while True:
    command =input('> ').lower()
    if command == 'help':
#        print("""               #remove this comment
#start - to start the car        #remove this comment
#stop - to stop the car          #remove this comment
#quit - to exit                  #remove this comment
#        """)                    #remove this comment
"""   elif command == 'start':  #remove this comments
        if( not started):
            print('Car started... Ready to go!')
            started = True
        else:
            print('CAR IS ALREADY STARTED!!!')
    elif command == 'stop':
        if(started):
            print('Car stopped.')
            started = False
        else:
            print('CAR IS ALREADY STOPED!!!!')
    elif command == 'quit':
        break
    else:
        print('I don\'t understand that ...')
"""

#For Loops
"""
#loop throwng a string
for item in 'Python':
    print(item)

#loop a list of strings
for item in ['Mosh', 'John', 'Sarah']:
    print(item)

#loop a list of numbers
for item in [1,2,3,4,5]:
    print(item)

#loop in a gange of numbers
for item in range(5, 10, 2):
    print(item)


#Exercise: calculate the total of an array
prices = [10, 20, 30]
totalPrice = 0
for price in prices:
    totalPrice += price
print(totalPrice)
print(f"Total: {totalPrice}")

"""

#Nested loops
"""
for x in range(4):
    #print(x)
    for y in range(3):
        print(f'({x},{y})')
"""

#Challenge
#Print out the follow shape
"""
XXXXX
XX
XXXXX
XX
XX
"""
numbers = [5, 2, 5, 2, 2]
#solution 1
"""
for numb in numbers:
    print('x'*numb)
"""
#solution 2
for numb in numbers:
    printVal = ''
    for item in range(numb):
        printVal +='x'
    print(printVal)
   
print("Testing conflits merge: remote")
