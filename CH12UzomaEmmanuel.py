'''
Name: Emmanuel Uzoma
Date: March 5, 2025
Program Topic: Inheritance, Objects/Classes, and Decision structure
Program Description: This program creates an Employee Weekly Pay Report System for ABC Corp using inheritance. 
                    It uses a base Employee class with name and department attributes, and a derived HourlyEmp class 
                    that adds hourly rate and hours worked. The program calculates weekly pay for each employee, 
                    including overtime pay for hours worked over 40, and displays the total weekly payroll.
'''

# CONSTANTS
TITLE = "Welcome to Employee Weekly Pay Report Program!\n"
REG_HOURS = 40
OT_RATE = 1.5
COL_TITLE = "\nEmployee Name    Department    Weekly Pay\n"
LINE = '-' * len(COL_TITLE)

# Employee super/base class
class Employee:
    def __init__(self, name, dept):
        self.__name = name
        self.__dept = dept
    
    # Getter methods
    def get_name(self):
        return self.__name
    
    def get_dept(self):
        return self.__dept
    
    # Setter methods
    def set_name(self, name):
        self.__name = name
    
    def set_dept(self, dept):
        self.__dept = dept
    
    # String representation method
    def __str__(self):
        return f"{self.__name}    {self.__dept}"

# HourlyEmp sub/derived Class
class HourlyEmp(Employee):
    def __init__(self, name, dept, rate, hours):
        # Call the parent class constructor
        super().__init__(name, dept)
        
        # Initialize HourlyEmp specific attributes
        self.__rate = rate
        self.__hours = hours
    
    # Getter methods
    def get_rate(self):
        return self.__rate
    
    def get_hours(self):
        return self.__hours
    
    # Setter methods
    def set_rate(self, rate):
        self.__rate = rate
    
    def set_hours(self, hours):
        self.__hours = hours
    
    # Calculate weekly pay with overtime consideration
    def calcWeeklyPay(self):
        if self.__hours <= REG_HOURS:
            weekly_pay = self.__hours * self.__rate
        else:
            # Calculate regular pay
            regular_pay = REG_HOURS * self.__rate
            # Calculate overtime pay
            overtime_hours = self.__hours - REG_HOURS
            overtime_pay = overtime_hours * self.__rate * OT_RATE
            weekly_pay = regular_pay + overtime_pay
        
        return weekly_pay
    
    # String representation method
    def __str__(self):
        # Get the base class string representation
        base_str = super().__str__()
        weekly_pay = self.calcWeeklyPay()
        return f"{base_str}    ${weekly_pay:.2f}"

# Function to display results
def displayResults(emp1, emp2, totalPay):
    print(TITLE)
    print(LINE)
    print(COL_TITLE)
    print(LINE)
    print(f"{emp1.get_name()}          {emp1.get_dept()}    ${emp1.calcWeeklyPay():.2f}")
    print(f"{emp2.get_name()}          {emp2.get_dept()}        ${emp2.calcWeeklyPay():.2f}")
    print(LINE)
    print(f"Total Weekly Pay: ${totalPay:.2f}")

# main function definition
def main():
    # Create employee objects
    emp1 = HourlyEmp("Mary", "Accounting", 20.5, 55)
    emp2 = HourlyEmp("Tuan", "Finance", 30, 40)
    
    # Calculate total pay
    totalPay = emp1.calcWeeklyPay() + emp2.calcWeeklyPay()
    
    # Display the results
    displayResults(emp1, emp2, totalPay)

# main function call
main()
