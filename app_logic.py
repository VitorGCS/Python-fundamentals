#logical operators
"""
has_high_income = True
has_good_credit = True

if not has_high_income and has_good_credit:
    print("Eligible for loan")


#Comparation operators
temperature = 30

if temperature != 30:
    print("It's a hot day")
else:
    print("It's not a hot day")
"""


name = "John Smith"
if len(name) <3:
    print("Name must be at least 3 character.")
elif len(name) >30:
    print("Name must be a maximum of 30 characters.")
else:
    print("Name looks good.")