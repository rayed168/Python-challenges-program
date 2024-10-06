import string
import random
length = int(input("Enter password length: "))
 
print('''Choose characters for password : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')
characterList = ""
while(True):
    choice = int(input("Pick a number : "))
    if(choice == 1):
        characterList += string.ascii_letters
    elif(choice == 2):
        characterList += string.digits
    elif(choice == 3):
         characterList += string.punctuation
    elif(choice == 4):
        break
password = []
 
for i in range(length):
    random_character = random.choice(characterList)
    password.append(random_character)
print("The random password is " + "".join(password))