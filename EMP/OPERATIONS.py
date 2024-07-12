#!/usr/bin/python3

from EMP import EMPLOYEE_MANAGEMENT

total_legal_days = 22

def get_employee_info(id):
    return EMPLOYEE_MANAGEMENT.get_employee(id)

def calculate_bonus(id):
    employee = EMPLOYEE_MANAGEMENT.get_employee(id)
    salary = float(employee.get('salary'))
    return (0.1*salary)

def calculate_discount(id):
    employee = EMPLOYEE_MANAGEMENT.get_employee(id)
    salary = float(employee.get('salary'))
    return (0.05*salary)

def calculate_remaining_days(id):
    global total_legal_days
    employee = EMPLOYEE_MANAGEMENT.get_employee(id)
    return (total_legal_days - employee.get('days of absence'))