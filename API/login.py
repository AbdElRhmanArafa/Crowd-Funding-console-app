
import csv


def logInSystem(Email, Password, file):
    """
    Return (list ): user information name email phone 
    Args:
        Email (string): _description_
        Password (string): _description_
        file (string): _description_
    """

    file += "user_information.csv"
    listOfUserInfo = []
    with open(file, 'r') as fileCvs:
        reader = csv.reader(fileCvs, delimiter=':')
        for row in reader:
            if row[2] == Email and row[3] == Password:
                listOfUserInfo.append(row[0])  # ? First Name
                listOfUserInfo.append(row[2])  # ? Email
                listOfUserInfo.append(row[4])  # ? Phone
                return listOfUserInfo
    return None
