import csv
import datetime


def createProject(DataBaseFile, projectListInformation):
    """
    This function creates a project The user can create
    a project fund raise campaign which contains:
    • User Name 
    • project Title
    • Details
    • Total target (i.e 250000 EGP)
    • Set start/end time for the campaign (validate the date formula)
    Args:
        DataBaseFile (string): file directory PATH 
        ProjectListInformation (list): list of Information
    """
    DataBaseFile += "/projects.csv"
    with open(DataBaseFile, 'a') as ProjectFile:
        writer = csv.writer(ProjectFile, delimiter=':')
        writer.writerow(projectListInformation)


def validateProjectData(user,DataBaseFile):
    """ 
    """
    projectInformation = []

    projectInformation.append(user)
    print("Please Enter Project Information: ")
    Titles = input("Please Enter Project Title: ")
    projectInformation.append(Titles)
    Details = input("Please Enter Project Details: ")
    projectInformation.append(Details)
    target = input("Please Enter Project target: ")
    if target.isdigit():
        projectInformation.append(target)
    else:
        print("Please Number ")
        return 0
    startDateStr = input("Enter the start date of project (YYYY-MM-DD): ")
    endDateStr = input("Enter the end date of project  (YYYY-MM-DD): ")
    try:
        startDate = datetime.datetime.strptime(startDateStr,"%Y-%m-%d")
        endDate = datetime.datetime.strptime(endDateStr,"%Y-%m-%d")
    except ValueError:
         print("Invalid date format. Please enter dates in YYYY-MM-DD format.")
    else:
        if startDate > endDate: 
             print("End date must be after start date.")
             return 0
        else:
            campaign_length = (endDate - startDate).days + 1
            projectInformation.append(startDateStr)
            projectInformation.append(endDateStr)
            projectInformation.append(campaign_length)
            createProject(DataBaseFile, projectInformation)
    return 1