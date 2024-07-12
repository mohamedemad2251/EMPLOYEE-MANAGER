#!/usr/bin/python3

from enum import Enum       #We'll make a state machine-designed code
from LOGIN import LOGIN     #Import the login module we created
import getpass              #To be able to conceal the password characters written (types nothing)
from EMP import EMPLOYEE_MANAGEMENT, OPERATIONS #Import from the package 'EMP' the 2 modules 

CLI_STATES = Enum('CLI_STATES',['LOGIN','USER','BLOCKED','EXIT'])  #Enum to have different states for the CLI
cli_state = CLI_STATES.LOGIN    #Initially, the state of the machine is "Login"

OPTIONS = Enum('OPTIONS',['INFO','MANAGEMENT','EXIT']) #Enum to select between showing different info (info/bonus/discount/holidays) & employee management (add/delete/update)
options_selection = 0   

INFO_OPTIONS = Enum('INFO_OPTIONS',['DISP','BONUS','DISCOUNT','HOLI','EXIT']) #Enum to select between different info options (info/bonus/discount/holidays)
info_options_selection = 0  

MAN_OPTIONS = Enum('MAN_OPTIONS',['ADD','DELETE','UPDATE','EXIT']) #Enum to select between different employee management options (add/delete/update)
man_options_selection = 0

UPDATE_OPTIONS = Enum('UPDATE_OPTIONS',['NAME','DEPARTMENT','SALARY','DAYS','EXIT'])

def initiateLogin():
    print("=================================================================\n\t\tWelcome To The Employee Manager!\n=================================================================")
    cli_password = input("Enter a password that'll be used for logging in: ")
    LOGIN.setLogin(cli_password)    #Sets login password for the first time

def cli_add_employee():
    id = input("\n\nEnter the employee's ID: ")
    while(not id.isdecimal() or (int(id) < 0)):
        id = input("ID must be bigger than or equals zero and contains numbers only, please re-enter: ")
    while(EMPLOYEE_MANAGEMENT.find_employee(int(id))):
        id = input("ID already exists, please re-enter: ")
    name = input("Enter the employee's name: ")
    while(not name.isalpha()):
        name = input("Name must be alphabets only! Please re-enter: ")
    department = input("Enter the employee's department: ")
    while(not department.isalpha()):
        department = input("Department must be alphabets only! Please re-enter: ")
    salary = input("Enter the employee's salary: ")
    while(not salary.isdecimal() or (int(salary) <= 0)):
        salary = input("Salary must be bigger than zero and contains numbers only, please re-enter: ")
    days_of_absence = input("Enter the employee's days of absence: ")
    while(not days_of_absence.isdecimal() or (int(days_of_absence) <= 0)):
        days_of_absence = input("Days of Absence must be bigger than zero and contains numbers only, please re-enter: ")
    EMPLOYEE_MANAGEMENT.add_employee(int(id),name,department,int(salary),int(days_of_absence))
    print("Added Successfully!")

def cli_delete_employee():
    id = input("Enter the employee's ID: ")
    while(not id.isdecimal() or (int(id) < 0)):
        id = input("ID must be bigger than or equals zero and contains numbers only, please re-enter: ")
    if(EMPLOYEE_MANAGEMENT.find_employee(int(id))):
        if(EMPLOYEE_MANAGEMENT.delete_employee(int(id))):
            print("Deleted Successfully!")
        else:
            print("Failed to delete! Returning to main menu!\n")

    else:
        print("Couldn't find the ID! Returning to main menu!\n")

def cli_update_employee():
    update_selection = 0
    id = input("Enter the employee's ID: ")
    while(not id.isdecimal() or (int(id) < 0)):
        id = input("ID must be bigger than or equals zero and contains numbers only, please re-enter: ")
    if(EMPLOYEE_MANAGEMENT.find_employee(int(id))):
        while(update_selection != UPDATE_OPTIONS.EXIT.value):
            print(f"\n\nSelect the info to update:\n[{UPDATE_OPTIONS.NAME.value}]Name\n[{UPDATE_OPTIONS.DEPARTMENT.value}]Department\n[{UPDATE_OPTIONS.SALARY.value}]Salary\n[{UPDATE_OPTIONS.DAYS.value}]Days of Absence\n[{UPDATE_OPTIONS.EXIT.value}]Return To Main Menu\nYour choice:")
            update_selection = int(input())
            while(update_selection != UPDATE_OPTIONS.NAME.value and update_selection != UPDATE_OPTIONS.DEPARTMENT.value and update_selection != UPDATE_OPTIONS.SALARY.value and update_selection != UPDATE_OPTIONS.DAYS.value and update_selection != UPDATE_OPTIONS.EXIT.value):
                update_selection = int(input())
            match update_selection:
                case UPDATE_OPTIONS.NAME.value:
                    name = input("Enter the new name: ")
                    while(not name.isalpha()):
                        name = input("Name must be alphabets only! Please re-enter: ")
                    if(EMPLOYEE_MANAGEMENT.update_employee(int(id),'name',name)):
                        print("Updated Name Successfully!")
                case UPDATE_OPTIONS.DEPARTMENT.value:
                    department = input("Enter the new department: ")
                    while(not department.isalpha()):
                        department = input("Department must be alphabets only! Please re-enter: ")
                    if(EMPLOYEE_MANAGEMENT.update_employee(int(id),'department',department)):
                        print("Updated Department Successfully!")
                case UPDATE_OPTIONS.SALARY.value:
                    salary = input("Enter the new salary: ")
                    while(not salary.isdecimal() or (int(salary) <= 0)):
                        salary = input("Salary must be bigger than zero and contains numbers only, please re-enter: ")
                    if(EMPLOYEE_MANAGEMENT.update_employee(int(id),'salary',int(salary))):
                        print("Updated Salary Successfully!")
                case UPDATE_OPTIONS.DAYS.value:
                    days_of_absence = input("Enter the new days of absence: ")
                    while(not days_of_absence.isdecimal() or (int(days_of_absence) <= 0)):
                        days_of_absence = input("Days of Absence must be bigger than zero and contains numbers only, please re-enter: ")
                    if(EMPLOYEE_MANAGEMENT.update_employee(int(id),'days of absence',int(days_of_absence))):
                        print("Updated Days of Absence Successfully!")
                case UPDATE_OPTIONS.EXIT.value:
                    pass
    else:
        print("Couldn't find the ID! Returning to main menu!\n")

def management_options():
    global cli_state
    global man_options_selection
    print(f"\n\nPlease select an option\n[{MAN_OPTIONS.ADD.value}]Add an Employee\n[{MAN_OPTIONS.DELETE.value}]Delete an Employee\n[{MAN_OPTIONS.UPDATE.value}]Update an Employee\n[{MAN_OPTIONS.EXIT.value}]Return to Main Menu\nYour choice: ")
    while( (man_options_selection != MAN_OPTIONS.ADD.value) and (man_options_selection != MAN_OPTIONS.DELETE.value) and (man_options_selection != MAN_OPTIONS.UPDATE.value) and (man_options_selection != MAN_OPTIONS.EXIT.value)):
        man_options_selection = int(input())
    match man_options_selection:
        case MAN_OPTIONS.ADD.value:
            cli_add_employee()
        case MAN_OPTIONS.DELETE.value:
            cli_delete_employee()
        case MAN_OPTIONS.UPDATE.value:
            cli_update_employee()
        case MAN_OPTIONS.EXIT.value:
            pass
    man_options_selection = 0

def info_options():
    global cli_state
    global info_options_selection
    print(f"\n\nPlease select an option\n[{INFO_OPTIONS.DISP.value}]Display Employee's Info\n[{INFO_OPTIONS.BONUS.value}]Calculate Bonus for Employee\n[{INFO_OPTIONS.DISCOUNT.value}]Calculate Discount for Employee\n[{INFO_OPTIONS.HOLI.value}]Show Legal Holidays for Employee\n[{INFO_OPTIONS.EXIT.value}]Return to Main Menu\nYour choice: ")
    while( (info_options_selection != INFO_OPTIONS.DISP.value) and (info_options_selection != INFO_OPTIONS.BONUS.value) and (info_options_selection != INFO_OPTIONS.DISCOUNT.value) and (info_options_selection != INFO_OPTIONS.HOLI.value) and (info_options_selection != INFO_OPTIONS.EXIT.value)):
        info_options_selection = int(input())
    match info_options_selection:
        case INFO_OPTIONS.DISP.value:
            id = input("Enter the employee's ID: ")
            while(not id.isdecimal() or (int(id) < 0)):
                id = input("ID must be bigger than or equals zero and contains numbers only, please re-enter: ")
            if(EMPLOYEE_MANAGEMENT.find_employee(int(id))):
                employee = OPERATIONS.get_employee_info(int(id))
                for key,value in employee.items():
                    print(f"{key}: {value}")
            else:
                print("Couldn't find ID!")
        case INFO_OPTIONS.BONUS.value:
            id = input("Enter the employee's ID: ")
            while(not id.isdecimal() or (int(id) < 0)):
                id = input("ID must be bigger than or equals zero and contains numbers only, please re-enter: ")
            if(EMPLOYEE_MANAGEMENT.find_employee(int(id))):
                print(f"Bonus = ${OPERATIONS.calculate_bonus(int(id))}")
            else:
                print("Couldn't find ID!")
        case INFO_OPTIONS.DISCOUNT.value:
            id = input("Enter the employee's ID: ")
            while(not id.isdecimal() or (int(id) < 0)):
                id = input("ID must be bigger than or equals zero and contains numbers only, please re-enter: ")
            if(EMPLOYEE_MANAGEMENT.find_employee(int(id))):
                print(f"Discount = ${OPERATIONS.calculate_discount(int(id))}")
            else:
                print("Couldn't find ID!")
        case INFO_OPTIONS.HOLI.value:
            id = input("Enter the employee's ID: ")
            while(not id.isdecimal() or (int(id) < 0)):
                id = input("ID must be bigger than or equals zero and contains numbers only, please re-enter: ")
            if(EMPLOYEE_MANAGEMENT.find_employee(int(id))):
                print(f"Legal Days Remaining = {OPERATIONS.calculate_remaining_days(int(id))}")
            else:
                print("Couldn't find ID!")
        case INFO_OPTIONS.EXIT.value:
            pass    #Intentional pass, this will get us back to the main menu
    info_options_selection = 0

def options():
    global cli_state
    global options_selection
    print(f"\n\nPlease select an option\n[{OPTIONS.INFO.value}]Information About Employees\n[{OPTIONS.MANAGEMENT.value}]Manage Employees\n[{OPTIONS.EXIT.value}]Exit\nYour choice: ")
    while( (options_selection != OPTIONS.INFO.value) and (options_selection != OPTIONS.MANAGEMENT.value) and (options_selection != OPTIONS.EXIT.value)):
        options_selection = int(input())
    match options_selection:
        case OPTIONS.INFO.value:
            info_options()
        case OPTIONS.MANAGEMENT.value:
            management_options()
        case OPTIONS.EXIT.value:
            cli_state = CLI_STATES.EXIT
    options_selection = 0

def application():
    global cli_state

    initiateLogin()
    while(True):
        match cli_state:
            case CLI_STATES.LOGIN:
                cli_password = getpass.getpass("Please enter the password (no characters will be shown): ")
                if(LOGIN.authenticate(cli_password)):
                    print("Logged In Successfully!\n\n")
                    print("=============================================\n\t\tWelcome, User!\n=============================================")
                else:
                        print("Wrong Password! Trials left: ",(LOGIN.getTotalAttempts() - LOGIN.getAttempts()))
            case CLI_STATES.BLOCKED:
                print("You are now blocked! The program will now exit!")
                cli_state = CLI_STATES.EXIT
            case CLI_STATES.USER:
                options()
            case CLI_STATES.EXIT:
                break
                    