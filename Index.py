
#? const global variables  
#? no const keyword variables in python so we can just make a global variable in upper case or make function return value    

from API import *
from API import Registration

# ,lastName,Email,Password
ROOTFIIE = os.path.dirname(__file__)
DataBaseFile = ROOTFIIE + os.sep + "Database" + os.sep
chooseWhatDoYouWant=0
separatorBetweenLine="*"*50



strMainScreen="""
\t 1- Registrations 
\t 0-Exit 
"""





strMainScreen+=separatorBetweenLine
while True:
    print (strMainScreen)
    choiceWhatDoYouWant= input("Please your choice ? ")
    if not choiceWhatDoYouWant.isdigit():
        print("Please enter a valid choice")
    elif int(choiceWhatDoYouWant)==1:
        Registration.RegisterIsValid(DataBaseFile)
    elif int(choiceWhatDoYouWant)==0:
        sys.exit("application will exit")

    