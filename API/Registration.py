from API import os,re,sys
""" 
the main goal of this code is to be reuseable 
"""
RULES = """
        • password must contain 1 number (0-9)
        • password must contain 1 uppercase letters
        • password must contain 1 lowercase letters
        • password must contain 1 non-alpha numeric number excepted :
        • password is 8-16 characters with no space

"""

def writeUserInformation(infoAboutUser,file):
    """
    this function just writes the user information in CVS file and the determined is :
    file order filed  (First Name,last Name , email, password , phone number)
    Args:
        infoAboutUser (dict): have user information and it's valid ready to add
        DataBaseFile (string): global data base file to write user information in right locations
    """
    
    
    with open(file,"a") as csvFile:
        for key in infoAboutUser:
            csvFile.write(infoAboutUser[key])
            if key != "phoneNumber":
                csvFile.write(" : ")
        csvFile.write("\n")



#! /****************************************************************/
def notReplacedValue(listOfDistinctInfo,file):
    """_summary_ this function may be not readable for human i work to improve it 
                 

    Args:
        listOfDistinctInfo (list ): element list of distinct can not repeated values in file
        DataBaseFile (_type_):file location 
    """
    with open(file, "r") as csvFile:    
        for line in csvFile:
            UserData = line.split(" : ")
            listOfDistinctInfo[2]+='\n'
            del UserData[1] #? delete last name from list
            del UserData[2] #? delete password from list
            for index,field in enumerate(UserData):
                if field==listOfDistinctInfo[index]:
                   print (listOfDistinctInfo[index]+" : is already  used try another one  ")
                   sys.exit()
                    


#! /****************************************************************/
def RegisterIsValid(DataBaseFile):
    """
     Validate information and store it in the dictionary.
    """
    listOfDistinctInfo=[]

    firstName = input("Enter First Name : ")
    pattern="[A-Za-z]{4,}"
    while  not re.fullmatch(pattern, firstName) :
        print("*Please enter a valid first name only letters allowed ")
        firstName = input("Enter First Name : ")
    listOfDistinctInfo.append(firstName)
    lastName = input("Enter Last Name : ")
    while not re.fullmatch(pattern, lastName) :
        print("*Please enter a valid Last name only letters allowed ")
        lastName = input("Enter valid Last Name : ")

    Email = input("Enter Email : ")
    pattern = "^[A-Za-z0-9\.\+_-]+@gmail.com"

    while not re.fullmatch(pattern, Email):
        print("*Please enter a valid email address")
        Email = input("Enter Email address : ")
    listOfDistinctInfo.append(Email)

    password = input("Password : ")
    pattern = "^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s])([^\s]){8,16}$"
    while not re.fullmatch(pattern, password):
        print("*Please enter a password that follows the Rule :\n\t "+RULES)
        password = input("Enter valid Password : ")

    rePassword = input("Re-Password : ")
    while not rePassword == password:
        print("*Please enter a matched password :")
        password = input("Enter match  Re-Password : ")

    phoneNumberValidInEg = input("Your Phone Number : ")
    pattern = "0{1}1{1}[5|0|1|2]{1}\d{8}"
    while not re.fullmatch(pattern, phoneNumberValidInEg):
        print("*Please enter a valid number in Egypt  :")
        phoneNumberValidInEg = input("Enter valid phone : ")
    listOfDistinctInfo.append(phoneNumberValidInEg)
    infoAboutUser = {"firstName": firstName, "lastName": lastName,
                     "email": Email, "password": password, "phoneNumber": phoneNumberValidInEg}
    # check if file exists 
    file=DataBaseFile+"user_information.csv"

    if  os.path.exists(file):
        notReplacedValue(listOfDistinctInfo,file)
    writeUserInformation(infoAboutUser,file)


    


        