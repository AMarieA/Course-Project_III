#ALaina Acton
#CIS 261
#Course Project Phase 4

from collections import UserList
from datetime import datetime

def CreateUsers():
    print('##### Create users, passwords, and roles #####')
    UserFile = open("Users.txt", "a+")
    while True:
        username = GetUserName()
        if (username.upper() == "END"):
            break
        userpwd = GetUserPassword()
        userrole = GetUserRole()
        
        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
        UserFile.write(UserDetail)
    
    UserFile.close()
    printuserinfo()
    
def GetUserName():
    username = input("Enter user name or 'End' to quit: ")
    return username

def GetUserPassword():
    pwd = input("Enter password: ")
    return pwd

def GetUserRole():
    userrole = input("Enter role (Admin or User): ")
    while True:
        if userrole.upper() == "ADMIN" or userrole.upper() == "USER":
            return userrole
        else:
            userrole = input("Enter role (Admin or User): ")
            
def printuserinfo():
    UserFile = open("Users.txt", "r")
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            break
        UserDetail = UserDetail.replace("\n", "")
        UserList = UserDetail.split("|")
        username = UserList[0]
        userpassword = UserList[1]
        userrole = UserList[2]
        print("Username: ", username, " Password: ". userpwd, " Role: ", userrole)
        
def Login():
    Userfile = open("Users.txt" "r")
    UserList = []
    UserName = input("Enter User Name: ")
    UserPwd = input("Enter Password: ")
    UserRole = "None"
    while True:
        UserDetail = Userfile.readline()
        if not UserDetail:
            return UserRole, UserName, UserPwd
        UserDetail = UserDetail.replace("\n", "")
        
        UserList = UserDetail.split("|")
        if UserName == UserList[0] and UserPwd == UserList[1]:
            UserRole = UserList[2] 
            return UserRole, UserName
    return UserRole, UserName
        


def GetempName():
    empname = input("Enter Employee name: ")
    return empname

def GetdatesWorked():
    fromdate = input("Enter the start date (mm/dd/yyyy): ")
    todate = input("Enter the end date (mm/dd/yyyy): ")
    return fromdate, todate

def GethoursWorked():
    hours = float((input("Enter the amount of hours worked: ")))
    return hours

def GethourlyRate():
    hourlyrate = float(input("Enter the hourly rate: "))
    return hourlyrate

def GettaxRate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate

def CalcTaxandNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printInfo(DetailsPrinted): #Establish a list and assign places.
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    EmpFile = open("Employees.txt", "r")
    while True:
        rundate = input("Enter start date for report (mm/dd/yyyy) or ALL for all data in file: ")
        if (rundate.upper() == "ALL"):
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Try again.")
            print()
            continue
    while True:
        EmpDetail = EmpFile.readline()
        if not EmpDetail:
            break
        EmpDetail = EmpDetail.replace("\n", "")
        
        EmpList = EmpDetail.split("|")
       
        fromdate = EmpList[0]
        if (str(rundate).upper() != "ALL"):
            checkdate = datetime.strptime(fromdate, "%m/%d/%Y")
            if (checkdate < rundate):
                continue
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]
    
        grosspay, incometax, netpay = CalcTaxandNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:.2f}")
        
        #calculating and adding to...keeping a count
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
    
        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHours"] = TotHours
        EmpTotals["TotGrossPay"] = TotGrossPay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNetPay"] = TotNetPay
        DetailsPrinted = True
    if (DetailsPrinted):
        PrintTotals(EmpTotals)
    else:
        print("No detail information to print")

def PrintTotals(EmpTotals):
    print()
    print(f"Total number of employess: {EmpTotals['TotEmp']}")
    print(f"Total hours worked: {EmpTotals['TotHours']}")
    print(f"Total Gross Pay: {EmpTotals['TotGrossPay']:,.2f}")
    print(f"Total Income Tax: {EmpTotals['TotTax']:,.1%}")
    print(f"Total Net Pay: {EmpTotals['TotNetPay']:,.2f}")
    
    
    
if __name__ == "__main__":
    CreateUsers()
    print()
    print("##### Data Entry #####")
    UserRole, UserName = Login()
    DetailsPrinted = False
    EmpTotals = {}
    if (UserRole.upp() == "NONE"):
        print(UserName, " is invalid.")
    else:
        if (UserRole.upper() == "ADMIN"):
            EmpFile = open("Employees.txt", "a+")
            while True:
                empname = GetempName()
                if (empname.upper() == "END"):
                    break
                fromdate, todate = GetdatesWorked()
                hours = GethoursWorked()
                hourlyrate = GethourlyRate()
                taxrate = GettaxRate()
        
                EmpDetail = fromdate, + "|" + todate, "|" + empname, "|" + hours, "|" + hourlyrate, "|" + taxrate, + "\n"
                EmpFile.write(EmpDetail)
                
            EmpFile.close()
    
        printInfo(DetailsPrinted)
   
    