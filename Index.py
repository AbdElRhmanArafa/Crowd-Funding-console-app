
# ? const global variables
# ? no const keyword variables in python so we can just make a global variable in upper case or make function return value

from API import *
from API import Registration
from API import login

# ,lastName,Email,Password
ROOTFIIE = os.path.dirname(__file__)
DataBaseFile = ROOTFIIE + os.sep + "Database" + os.sep
chooseWhatDoYouWant = 0
separatorBetweenLine = "*"*50


strMainScreen = """
\t 1- Registrations 
\t 2- Login
\t 0-Exit 
"""

strMainLoginScreen = """
\t  Welcome {} , in our System Crowd-Funding console 
\t  1- Create Project 
\t  2- view All project 
\t  3- view My Project
\t  4- delete Project
\t  5- Log Out
\t  0-Exit 
"""

strMainScreen += separatorBetweenLine
userInfoSection = []
while True:
    if userInfoSection:
        print(strMainLoginScreen.format(userInfoSection[0]))
        choiceWhatDoYouWant = input("Please your choice ? ")

    else:
        print(strMainScreen)
        choiceWhatDoYouWant = input("Please your choice ? ")
        if not choiceWhatDoYouWant.isdigit():
            print("Please enter a valid choice")
        elif int(choiceWhatDoYouWant) == 1:
            Registration.RegisterIsValid(DataBaseFile)
        elif int(choiceWhatDoYouWant) == 2:
            Email = input("please enter your mail : ")
            password = input("please enter your password : ")
            userInfoSection = login.logInSystem(Email, password, DataBaseFile)
            if userInfoSection == None:
                print("invalid user or password please try again");
        elif int(choiceWhatDoYouWant) == 0:
            sys.exit("application will exit")