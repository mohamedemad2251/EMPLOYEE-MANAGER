#!/usr/bin/python3

#------------------------------------EMP_default VALUES & INITIALIZATIONS------------------------------------
employee_list = []  #List of all employees (Should be empty at first)
#------------------------------------------------------------------------------------------------------------

def find_employee(id):
    global employee_list
    if(len(employee_list)):
        for employee in employee_list:
            employee_id = dict(employee).get('id')
            if(int(employee_id) == id):
                return True
        return False
    else:
        return False
    
def get_employee(id):
    global employee_list
    if(find_employee(id)):
        for employee in employee_list:
            employee_id = dict(employee).get('id')
            if(int(employee_id) == id):
                return employee
    else:
        return dict(None)

def add_employee(id,name="N/A",department="N/A",salary=0,days_of_absence=0):
    global employee_list
    employee = {'id':id,'name':name,'department':department,'salary':salary,'days of absence':days_of_absence}
    employee_list.append(employee)

def delete_employee(id):
    global employee_list
    if(len(employee_list)):
        for employee in employee_list:
            employee_id = dict(employee).get('id')
            if(int(employee_id) == id):
                employee_list.remove(employee)
                return True
        return False
    else:
        return False
    
def update_employee(id,key,value):
    global employee_list
    for employee in employee_list:
        if(id == dict(employee).get('id')):
            index = employee_list.index(employee)
            employee_list[index].update({key:value})
            return True
    return False
