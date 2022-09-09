import random, string

def passwordCreator(length):
    # defines the elements need for the password, which includes case-sensitive letters, numbers, and symbols.
    lowercaseLetters = string.ascii_lowercase # all the lowercase letters in the alphabet
    uppercaseLetters = string.ascii_uppercase # all the uppercase letters in the alphabet
    numbers = string.digits # all the numbers from 0-9
    symbols = string.punctuation # symbols such as !@#$%^&*()-=+,.<>/?;:'"[{}]\|`~

    # In order to create the password we must combine all of the elements together.
    all = lowercaseLetters + uppercaseLetters + numbers + symbols

    # randomly jumbles together the elements all together
    combined = random.sample(all, length)

    # joins the entire password together and presents it to the user
    password = ''.join(combined)
    return password

def passwordStorage(password, answer1):
    passwordStorage = open('Password Storage.txt', 'a') # Creates the folder for the password storage    
    passwordStorage.write('Password:| ' + password + ' | <- ' + answer1 + '\n') # if they like it it will output the password into 
    passwordStorage.close()