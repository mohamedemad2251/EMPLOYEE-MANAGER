#!/usr/bin/python3

from CLI import CLI

login_password = "0000" #Default password
login_attempts = 0
total_login_trials = 3      #Maximum number of trials allowed (Configurable)

def setLogin(password):
    global login_password

    login_password = password

def getTotalAttempts():
    return total_login_trials

def getAttempts():
    return login_attempts

def authenticate(password):
    global login_password
    global login_attempts
    global total_login_trials
    
    if login_attempts < total_login_trials:
        if password == login_password:
            CLI.cli_state = CLI.CLI_STATES.USER
            return True
        else:
            login_attempts += 1
            if(login_attempts < total_login_trials):
                CLI.cli_state = CLI.CLI_STATES.LOGIN
            else:
                CLI.cli_state = CLI.CLI_STATES.BLOCKED
            return False