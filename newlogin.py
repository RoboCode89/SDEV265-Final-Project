import sqlite3 #importing sqlite for database
#Create Employee class with first name, last name and id parameters.
class Employee():
    def __init__(self, fname, lname, user_id):
        self.fname = fname
        self.lname = lname
        self.user_id = user_id
#Register class for employee registration        
class Register():
    def __init__(self, Employee):
        self.Employee = Employee
    #method to register the employees   
    def register(self):
        db_conn = sqlite3.connect('employee.db') #connecting to database
        db_cur = db_conn.cursor() #creating cursor object
        #creating employees table if one doesnt exist with columns to store employees first and last name along with ID.
        db_cur.execute('''CREATE TABLE IF NOT EXISTS employees
                       (First_Name text, Last_Name text, Employee_ID integer PRIMARY KEY)''')
        db_cur.execute('SELECT * FROM employees WHERE "Employee_ID"=?', (self.Employee.user_id,))
        data = db_cur.fetchone() #checking db rows for matching ID
        if data: #checking if data was found
            print("ID already exists.") #if data found tell user it already exists
            return
        #adding new employee information to database if it doesnt exist
        db_cur.execute('INSERT INTO employees (First_Name, Last_Name, Employee_ID) VALUES (?,?,?)',
                       (self.Employee.fname, self.Employee.lname, self.Employee.user_id,))
        
        db_conn.commit() #commit changes
        db_conn.close() #close database connection
 #class for employee login       
class Login():
    def __init__(self, Employee):
        self.Employee = Employee
     #method for login   
    def employee_login(self):
        db_conn = sqlite3.connect('employee.db')
        db_cur = db_conn.cursor()
        #check if id is in database
        db_cur.execute('SELECT * FROM employees WHERE "Employee_ID"=?', (self.Employee.user_id,))
        data = db_cur.fetchone()
        if data:
            print("Login Successful") #if credentials are correct login
        else:
            print("Login Failed") #credentials are incorrect
        db_conn.close()
 #input validation for first and last name entry
def check_credentials_and_login():      
    while True:
        fname = input("First name: ")
        lname = input("Last name: ")
        if not fname.isalpha():
            print("Invalid first name! Please enter alphabetic characters only. ")
        elif not lname.isalpha():
            print("Invalid last name! Please enter alphabetic characters only. ")
        else:
            break
#input validation for user id being integer
    while True:
        try:
            user_id = int(input("Enter 4 digit pin: "))
            if user_id < 1000 or user_id > 9999:
             print("Please enter a 4 digit pin! ")
            else:
                break
        except ValueError:
            print("Incorrect input, please enter numbers only")
#create object for employee        
    employee = Employee(fname, lname, user_id)
#registering the employee
    register = Register(employee)
    register.register()
#logging in employee
    login = Login(employee)
    login.employee_login()
        
        