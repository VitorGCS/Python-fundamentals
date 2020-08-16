#Dictionaries
# key-value pairs, don't enable keys repeated
"""
customer = {
    "name":"John Smith",
    "age":30,
    "is_verified":True
}
#access to values
print(customer["name"])
print(customer.get("name"))
print(customer.get("Name"))#if don't find, return "None"
print(customer.get("Name", "Default value insted None"))

#update/ add values
customer["name"] = "Vitor Gil"
customer["surname"] = "Silva"
print(customer)
"""
#Challenge
#Write a program that asks for a phoneNumber in digites and respond with words
"""
numberdic = {
    '1': "one",
    '2': "two",
    '3':"three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven",
    '8': "eight",
    '9': "nine"
}
number = input("Phone:")
numberWords = ""
for item in number:
    numberWords += numberdic[item]+" "
print(numberWords)
"""

#coding to translate simbol to imoji
message = input(">")
words = message.split(' ')
print(words)
emojies = {
    ":)": "😊",
    ":(": "😒"
}

output = ""
for word in words:
    output += emojies.get(word, word)+' '
print(output)