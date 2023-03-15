
import csv
def logInSystem(Email,Password,file):
    """

    Args:
        Email (string): _description_
        Password (string): _description_
        file (string): _description_
    """
    file+="user_information.csv"
    try:
        # Opening the file
        f = open(file, 'r')
        # Reading the file
        lines = csv.reader(f,delimiter=':')
        # Closing the file
        f.close()
    except IOError:
        print("Error opening the file")
        return 0
    # Checking if the file is empty
    if len(lines) == 0:
        print("No User found please register first  ")
        return 0
    # Checking if the file is not empty
    if len(lines) > 0:
        # Checking if the file contains the email
        for line in lines:
            if Email == line[2]:
                # Checking if the file contains the password
                if Password == line[3]:
                    print("Login Successful")
                    return 1
                else:
                    print("Wrong Password")
                    return 0
            else: 
                print('user not found')
                return 0
