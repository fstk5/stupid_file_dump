#change the numeral of how many times you've opened this
#LI
#THIS TEXT MUST ALWAYS GO LAST OR WHEN THE PROGRAM EXITS!!!!!!!
#readAdmin.close()
#readfk5.close()

#Importing libraries or whatever the hell they're called

import os
import time
import hashlib
import getpass
import sys

#Defining the animation for the loading screen thingy

def coolAnimationPart():
    print("Please wait, loading file... |")
    time.sleep(.25)
    os.system('cls')
    print("Please wait, loading file... /")
    time.sleep(.25)
    os.system('cls')
    print("Please wait, loading file... -")
    time.sleep(.25)
    os.system('cls')
    print("Please wait, loading file... \\")
    time.sleep(.25)
    os.system('cls')
    print("Please wait, loading file... |")
    time.sleep(.25)
    os.system('cls')
    print("Please wait, loading file... /")
    time.sleep(.25)
    os.system('cls')
    print("Please wait, loading file... -")
    time.sleep(.25)
    os.system('cls')
    print("Please wait, loading file... \\")
    time.sleep(.25)
    os.system('cls')

#The actual full animation also defining the fileLoaded variable

def coolAnimationFull():
    global fileLoaded
    coolAnimationPart()
    coolAnimationPart()
    coolAnimationPart()
    coolAnimationPart()
    coolAnimationPart()
    fileLoaded = True
fileLoaded = False
isUsernameCorrect = False
isPasswordCorrect = False
global fk5, admin, currentUser
fk5 = "fk5"
admin = "admin"

#Code for logins: coolUsernameThing() asks the user their username

currentUser = "placeholder"
def coolUsernameThing():
    inputtedUsername = input("Please enter username. ")
    global isUsernameCorrect
    if inputtedUsername == fk5:
        print("Welcome, fk5.")
        time.sleep(1)
        currentUser = inputtedUsername
        isUsernameCorrect = True
    elif inputtedUsername == admin:
        print("Welcome, System Administrator.")
        time.sleep(1)
        os.system('cls')
        currentUser = inputtedUsername
        isUsernameCorrect = True
    else:
        print("User not found.")
        isUsernameCorrect = False

#keep asking for the username until is uses the correct one

while isUsernameCorrect == False:
    coolUsernameThing()

passwordEncryptionKey = getpass.getpass("Please enter your password encryption key.\nIf this key is incorrect, the password will not decrypt correctly and you will not be able to enter your account.\n")

#Get and assign user passwords to variables
#P.S. you aint getting the passwords that easy ;)

adminPassword = 'adminPassword.txt'
fk5Password = 'fk5Password.txt'

readAdmin = open(adminPassword, 'r')
readfk5 = open(fk5Password, 'r')

sha256Admin = hashlib.sha256(readAdmin)
sha256fk5 = hashlib.sha256(readfk5)

adminPWDData = readAdmin.read()
fk5PWDData = readfk5.read()

decryptedfk5Password = fk5PWDData.aes_decrypt(passwordEncryptionKey, commit=True)
decryptedAdminPassword = adminPWDData.aes_decrypt(passwordEncryptionKey, commit=True)

if adminPWDData or fk5PWDData == "":
    readAdmin.close()
    readfk5.close()
    sys.exit("Critical files damaged and/or deleted. Exiting file...")
else:
    os.system('cls')

if sha256Admin != "7e41e166f2218f01e6ba65947be5c1fcef5ce093a00e13a1e7429c5bc33bf44f":
    readAdmin.close()
    readfk5.close()
    sys.exit("Critical files damaged and/or deleted. Exiting file...")
else:
    os.system('cls')

if sha256fk5 != "6220d1f8c3b624cc0814611eb24929a1c9de10ba427c2d0546c8d09bee495c1f":
    readAdmin.close()
    readfk5.close()
    sys.exit("Critical files damaged and/or deleted. Exiting file...")
else:
    os.system('cls')

#same as coolUsernameThing(), but for the password

def coolPasswordThing():
    passwd = getpass.getpass("Please enter password. ")
    global isPasswordCorrect
    if currentUser == fk5:
        def fk5Authentication():
            if passwd == decryptedfk5Password:
                print("User fk5 authenticated.")
                time.sleep(1)
                os.system('cls')
                coolAnimationFull()
                isPasswordCorrect = True
            else:
                print("Sorry, that password is incorrect.")
        while isPasswordCorrect == False:
            fk5Authentication()
    elif currentUser == admin:
        def adminAuthentication():
            if passwd == adminPWDData:
                print("System Administrator authenticated.")
                time.sleep(1)
                os.system('cls')
                coolAnimationFull()
                isPasswordCorrect = True
            else:
                print("Sorry, that password is incorrect.")
        while isPasswordCorrect == False:
            adminAuthentication()
    elif currentUser == "boioioioioioioioioiooioioioioioioioioioioioiooioiioiioioong":
        os.system('cls')
        howTFDidYouGetHere = getpass.getpass("How did you get here?")
        if howTFDidYouGetHere == "321654978123456789":
            print("I don't even know how you got that number.\nJust take the admin account.")
            time.sleep(3)
            currentUser = admin
        else:
            readAdmin.close()
            readfk5.close()
            os.system('cls')
            sys.exit("Get out.")

#loop for password thing

while isPasswordCorrect == False:
    coolPasswordThing()
os.system('cls')

#gets decryption key for files

global decypherKey
def fileDecypher():
    os.system('cls')
    if currentUser == admin or fk5:
        os.system('cls')
        decypherKey = getpass.getpass("Input file decypher key.\n")
        os.system('cls')
    else:
        os.system('cls')
        print("Ok, how are you even doing this?")
        time.sleep(1)
        os.exit(1)
    def recheck():
        recheckVar = ("The decypher key length is " + len(decypherKey) + " characters long.\nDo you want to continue?\nThe key should be 32 characters long.\n")
        if recheckVar == "Y" or "y" or "yes":
            os.system('cls')
        elif recheckVar == "N" or "n" or "no":
            print("Restarting check...")
            time.sleep(1)
            fileDecypher()
        else:
            print("Invalid answer.")
            recheck()

fileDecypher()

#defines the file vault initialization

global isInputCorrect
def fileVaultInit():
    readfk5.close()
    readAdmin.close()
    print("Welcome to your file vault, " + currentUser + "\n")
    global ask
    ask = input("What would you like to do?\n1: Open a file\n2: Delete a file\n\nUse Ctrl C to exit")
    isInputCorrect = False

#defining the options

def fileViewer():
    os.system('cls')
    print("What file would you like to view?")
def fileDeleter():
    os.system('cls')
    print("What file would you like to delete?")

#defines the file vault option backend

isInputCorrect = False
def fileVaultDecision():
    if ask == 1:
        os.system('cls')
        fileViewer()
        isInputCorrect = True
    elif ask == 2:
        os.system('cls')
        fileDeleter()
        isInputCorrect = True
    else:
        os.system('cls')
        print("Invalid Option.")
        input("Press any key to continue...")
        os.system('cls')

#uses a loop for the file vault until it returns a correct option
    
def fileVaultDecisionLoop():
    while isInputCorrect == False:
        fileVaultInit()
        fileVaultDecision()