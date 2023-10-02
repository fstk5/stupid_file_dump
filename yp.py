#change the numeral of how many times you've opened this
#XXXIX
#THIS TEXT MUST ALWAYS GO LAST OR WHEN THE PROGRAM EXITS!!!!!!!
#readAdmin.close()
#readfk5.close()

#Importing libraries or whatever the hell they're called

import os
import time
from securefile import Encrypt
import hashlib
import sys

#checking that threading'll work

global cpuCheckCorrect
def cpuCheckAsk():
    global cpuCheck
    print("Please ensure your CPU has at least 2 threads, or a single-core CPU with hyperthreading enabled.")
    cpuCheck = input("\nDo you have one of these? y or n")
def cpuCheckActualCheck():
    if cpuCheck == "y":
        os.system('cls')
        print("Input accepted.")
        time.sleep(1)
        os.system('cls')
        global cpuCheckCorrect
        cpuCheckCorrect = True
    elif cpuCheck == "n":
        sys.exit("cpuCheckActualCheck() failed.")
    else:
        print("Invalid answer.")
cpuCheckCorrect = False
while cpuCheckCorrect == False:
    cpuCheckAsk()
    cpuCheckActualCheck()

#Get and assign user passwords to variables
#P.S. you aint getting the passwords that easy ;)

hell = 4823056873426594372865487380256347265748301632874061
heaven = 43789201758921096372410392756726437896304320240437295401545490
mortal = 9230293290328931574895065347652736481039248072375248632164132
immortal = 432871905830275215
free = 32189704389470144893704178439017825217
world = mortal * immortal
freeme = free * mortal
final = freeme + world * heaven / hell
final2 = final * final / final / final / final + final + final - final
final3 = final2 * final
final4 = final * final2 / final3
theKey = final4 * final4 / final / final2 / final3 / final4

adminPassword = 'adminPassword.txt'
fk5Password = 'fk5Password.txt'

readAdmin = open(adminPassword, 'r')
readfk5 = open(fk5Password, 'r')

sha256Admin = hashlib.sha256(readAdmin)
sha256fk5 = hashlib.sha256(readfk5)

adminPWDData = readAdmin.read()
fk5PWDData = readfk5.read()

filefk5 = Encrypt(fk5Password, delimiter=':')
fileadmin = Encrypt(adminPassword, delimiter=':')

decryptedfk5Password = filefk5.aes_decrypt(theKey, commit=True)
decryptedAdminPassword = fileadmin.aes_decrypt(theKey, commit=True)

if adminPWDData or fk5PWDData == "":
    readAdmin.close()
    readfk5.close()
    sys.exit("Critical files damaged and/or deleted. Exiting file...")
else:
    os.system('cls')

if sha256Admin != "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918":
    readAdmin.close()
    readfk5.close()
    sys.exit("Critical files damaged and/or deleted. Exiting file...")
else:
    os.system('cls')

if sha256fk5 != "711faa969abbf8f95f05aa2f2e2b03662febfc1c942f5568f9d0d155c4c9860f":
    readAdmin.close()
    readfk5.close()
    sys.exit("Critical files damaged and/or deleted. Exiting file...")
else:
    os.system('cls')

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
        print("Incorrect Username.")
        isUsernameCorrect = False

#keep asking for the username until is uses the correct one

while isUsernameCorrect == False:
    coolUsernameThing()

#same as coolUsernameThing(), but for the password

def coolPasswordThing():
    passwd = input("Please enter password. ")
    global isPasswordCorrect
    if currentUser == fk5:
        def fk5Authentication():
            if passwd == fk5PWDData:
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
        howTFDidYouGetHere = input("How did you get here?")
        if howTFDidYouGetHere == "2215189394":
            print("I don't even know how you got that number.\nJust take the admin account.")
            time.sleep(3)
        else:
            readAdmin.close()
            readfk5.close()
            os.system('cls')
            sys.exit("Get out.")

#loop for password thing

while isPasswordCorrect == False:
    coolPasswordThing()
os.system('cls')

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
    print("What file would you like to view?")
def fileDeleter():
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