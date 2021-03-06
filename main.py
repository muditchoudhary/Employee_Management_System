from cgitb import text
from distutils import command
from logging import exception
from time import sleep
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from turtle import width
from mysql import connector
import mysql.connector
from mysql.connector import connection_cext
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import column

class EmployeeManagement:

    def __init__(self, root):
        root.title("Employee Management System")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.employees_data = []

        # Style object
        s = ttk.Style()
        s.configure('welcomeFrame.TFrame', background = '#bfbaba')
        s.configure('mainframe.TFrame', background='red')
        s.configure('label.TLabel', font=('Times New Roman', 30))
        s.configure('myLabel.TLabel', font = ('Times New Roman', 20))
        s.configure('admin.TFrame', background='green')
        s.configure('employee_data.TFrame', background='yellow')
        s.configure('addemp_fr.TFrame', background='pink')
        s.configure('delemp_fr.TFrame', background='orange')
        s.configure('upateemp_fr.TFrame', background='lightblue')
        s.configure('ademp.TButton', font=('Times New Roman', 30))
        s.configure('back.TButton', font=('Times New Roman', 15))
        s.configure('list.TButton', font=('Times New Roman', 15))
        s.configure('h1.TLabel', font = ('Times New Roman', 35, 'bold'))
        s.configure('h2.TLabel', font = ('Times New Roman', 27, 'bold'))
        s.configure('h3.TLabel', font = ('Times New Roman', 19, 'bold'))

        # Welcome screen main frame
        self.welcome_screen_fr = ttk.Frame(root, style='welcomeFrame.TFrame')
        # Creating main frame
        self.mainframe = ttk.Frame(root, style='mainframe.TFrame')
        # Admin window frame
        self.admin = ttk.Frame(root, style='admin.TFrame')
        # View employee data frame
        self.employees_data_fr = ttk.Frame(root, style='employee_data.TFrame')
        # Add an employee main frame
        self.addemp_main_fr = ttk.Frame(root, style='addemp_fr.TFrame')
        # Delete an employee main frame
        self.delemp_main_fr = ttk.Frame(root, style='delemp_fr.TFrame')
        # Update employee data main frame
        self.updateemp_main_fr = ttk.Frame(root, style='upateemp_fr.TFrame')

        # Render main frames
        for frame in (self.welcome_screen_fr, self.mainframe, self.admin, self.employees_data_fr, self.addemp_main_fr, self.delemp_main_fr, self.updateemp_main_fr):
            frame.grid(column=0, row=0, sticky=(N,S,E,W))
            frame.columnconfigure(0, weight=1)
            frame.rowconfigure(0, weight=1)

        # Welcome screen sub frame
        welcome_sub_fr = ttk.Frame(self.welcome_screen_fr, borderwidth=2, relief='sunken', padding=50)
        welcome_sub_fr.grid(column=0, row=0)
        welcome_sub_fr.columnconfigure(0, weight=1)
        welcome_sub_fr.rowconfigure(0, weight=1)

        ttk.Label(welcome_sub_fr, text='Welcome to', style='h1.TLabel').grid(column=0, row=0)
        ttk.Label(welcome_sub_fr, text='Employee Management System', style='h1.TLabel').grid(column=0, row=1)
        ttk.Label(welcome_sub_fr, text='CBSE AISSCE PROJECT', style='h2.TLabel').grid(column=0, row=2)
        ttk.Label(welcome_sub_fr, text='I.P. (2021-2022)', style='h2.TLabel').grid(column=0, row=3)

        ttk.Label(welcome_sub_fr, text='Developed by : Mudit Choudhary', style='h3.TLabel').grid(column=0, row=4)
        ttk.Label(welcome_sub_fr, text='Class 12 - C', style='h3.TLabel').grid(column=0, row=5)
        ttk.Label(welcome_sub_fr, text='Kendriya Vidhalaya No.4', style='h3.TLabel').grid(column=0, row=6)


        ttk.Button(welcome_sub_fr, text='Continue', style='back.TButton', command=self.raiseLogInScreen).grid(column=0, row=7)
        
        # Final touches
        for child in welcome_sub_fr.winfo_children():
            child.grid_configure(padx=80, pady=10)

        # Content frame (part of mainframe window from line 31 to 57)
        content_frame = ttk.Frame(self.mainframe, padding=60, borderwidth=2, relief='sunken')
        content_frame.grid(column=0, row=0)
        content_frame.columnconfigure(0, weight=1)
        content_frame.rowconfigure(0, weight=1)
        # Name label
        ttk.Label(content_frame, text="Name", font=('Times New Roman', 30)).grid(column=1, row=1, sticky=E)
        # Name Entry widget
        self.name = StringVar()
        self.name_entry = ttk.Entry(content_frame, width=30, textvariable=self.name, font=('Times New Roman', 15))
        self.name_entry.grid(column=2, row=1, sticky=(E, W))

        # Password label
        ttk.Label(content_frame, text="Password", font=('Times New Roman', 30)).grid(column=1, row=2, sticky=E)
        # Password Entry widget
        self.password = StringVar()
        self.password_entry = ttk.Entry(content_frame, width=16, textvariable=self.password,  font=('Times New Roman', 15))
        self.password_entry.grid(column=2, row=2, sticky=(E, W))
        self.password_entry.configure(show="*")

        # Log in button
        ttk.Button(content_frame, text="Log in", command=self.logIn, style='back.TButton').grid(column=2, row=3, sticky=(E, W))
        ttk.Button(content_frame, text="Go back", command=lambda: self.goBack(self.welcome_screen_fr), style='back.TButton').grid(column=2, row=4)
        
        # Final touches
        for child in content_frame.winfo_children():
            child.grid_configure(padx=15, pady=15)
        self.name_entry.focus()

        # Start the welcome screen first
        self.showFrame(self.welcome_screen_fr)

        # Admin window contents (part of admin window from line 85 to 118)
        admin_content_frame = ttk.Frame(self.admin, padding=30, borderwidth=2, relief='sunken')
        admin_content_frame.grid(column=0, row=0)
        admin_content_frame.columnconfigure(0, weight=1)
        admin_content_frame.rowconfigure(0, weight=1)

        # Employee menu frame
        employee_menu_fr = ttk.Frame(admin_content_frame, borderwidth=2, relief='sunken')
        employee_menu_fr.grid(column=0, row=0)
        ttk.Label(employee_menu_fr, text='Employee Menu', style='label.TLabel').grid(column=0, row=0)
        ttk.Button(employee_menu_fr, text='1. View employees data', style='list.TButton', command=self.raiseViewEmployeeWin).grid(column=0, row=1)
        ttk.Button(employee_menu_fr, text='2. Add a new employee', style='list.TButton', command=self.riaseAddempWin).grid(column=0, row=2)
        ttk.Button(employee_menu_fr, text='3. Delete an employee', style='list.TButton', command=self.raiseDeleteEmpWin).grid(column=0, row=3)
        ttk.Button(employee_menu_fr, text='4. Update data of an employee', style='list.TButton', command=self.raiseUpdateEmpWin).grid(column=0, row=4)
        # Graph menu frame
        graph_menu_fr = ttk.Frame(admin_content_frame, borderwidth=2, relief='sunken')
        graph_menu_fr.grid(column=1, row=0, sticky=(N,S))
        ttk.Label(graph_menu_fr, text='Graphical view menu', style='label.TLabel').grid(column=0, row=0)
        ttk.Button(graph_menu_fr, text='1. Total Salary Grpah', style='list.TButton', command=self.drawTotalSalaryGraph).grid(column=0, row=1)
        ttk.Button(graph_menu_fr, text='2. Total Bonus Graph', style='list.TButton', command=self.drawTotalBonusGraph).grid(column=0, row=2)
        ttk.Button(graph_menu_fr, text='3. Average Salary Graph', style='list.TButton', command=self.drawAvgSalaryGraph).grid(column=0, row=3)
        ttk.Button(graph_menu_fr, text='4. Average Bonus Graph', style='list.TButton', command=self.drawAvgBonusGraph).grid(column=0, row=4)

        # Go back button
        back_btn = ttk.Button(admin_content_frame, text='Go back', command=lambda: self.goBack(self.mainframe), style='back.TButton')
        back_btn.grid(column=0, row=1, columnspan=2, sticky=(E,W))

        # Final touches
        for child in admin_content_frame.winfo_children():
            child.grid_configure(padx=20, pady=20)
        for child in employee_menu_fr.winfo_children():
            child.grid_configure(padx=6, pady=12)
        for child in graph_menu_fr.winfo_children():
            child.grid_configure(padx=6, pady=12)

        # View employess data window contents (from line 136 to 152 )
        # Adding a canvas for data_content_fr
        self.my_canvas = Canvas(self.employees_data_fr)
        self.my_canvas.grid(column=0, row=0, sticky=(N, S, E, W))
        self.my_canvas.rowconfigure(0, weight=1)
        self.my_canvas.columnconfigure(0, weight=1)
        # Adding scrollbar
        my_scrollbar = Scrollbar(self.employees_data_fr, orient=VERTICAL, command=self.my_canvas.yview)
        my_scrollbar.grid(row=0, column=1, sticky=(N,S))
        # Configure the scrollbar
        self.my_canvas.configure(yscrollcommand=my_scrollbar.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion= self.my_canvas.bbox('all')))

        self.data_content_fr = ttk.Frame(self.my_canvas, padding=15, borderwidth=2, relief='sunken')
        # packing data cotent frame
        self.my_canvas.create_window((0,0), window=self.data_content_fr, anchor='nw')

        # Go back button
        ttk.Button(self.employees_data_fr, text='Go back', command=lambda: self.destroyLayoutGoBack(self.admin, self.data_content_fr), style='back.TButton').grid(row=1, column=0, sticky=(E,W), pady=15)

        # Add an employee subframe window
        addemp_sub_fr = ttk.Frame(self.addemp_main_fr, padding=15, borderwidth=2, relief='sunken')
        addemp_sub_fr.grid(column=0, row=0)
        addemp_sub_fr.columnconfigure(0, weight=1)
        addemp_sub_fr.rowconfigure(0, weight=1)

        # Adding column heading
        ttk.Label(addemp_sub_fr, width=20, text='EId', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=0)
        ttk.Label(addemp_sub_fr, width=20, text='Name', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=1)
        ttk.Label(addemp_sub_fr, width=20, text='Gender', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=2)
        ttk.Label(addemp_sub_fr, width=20, text='Age', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=3)
        ttk.Label(addemp_sub_fr, width=20, text='Salary', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=4)
        ttk.Label(addemp_sub_fr, width=20, text='Bonus', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=5)
        ttk.Label(addemp_sub_fr, width=20, text='Department', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=6)
        
        # Adding entry label for taking input from user
        # Eid entry label
        self.eid = IntVar()
        self.eid_entry = ttk.Entry(addemp_sub_fr, width=20, textvariable=self.eid)
        self.eid_entry.grid(column=0, row=1)
        # Name entry label
        self.emp_name = StringVar()
        self.emp_entry = ttk.Entry(addemp_sub_fr, width=20, textvariable=self.emp_name)
        self.emp_entry.grid(column=1, row=1)
        # Gender entry label
        self.gender = StringVar()
        self.gender_entry = ttk.Entry(addemp_sub_fr, width=20, textvariable=self.gender)
        self.gender_entry.grid(column=2, row=1)
        # Age entry label
        self.age = IntVar()
        self.age_entry = ttk.Entry(addemp_sub_fr, width=20, textvariable=self.age)
        self.age_entry.grid(column=3, row=1)
        # Salary entry label
        self.salary = IntVar()
        self.salary_entry = ttk.Entry(addemp_sub_fr, width=20, textvariable=self.salary)
        self.salary_entry.grid(column=4, row=1)
        # Bonus entry label
        self.bonus = IntVar()
        self.bonus_entry = ttk.Entry(addemp_sub_fr, width=20, textvariable=self.bonus)
        self.bonus_entry.grid(column=5, row=1)
        # Department entry label
        self.depatment = StringVar()
        self.depatment_entry = ttk.Entry(addemp_sub_fr, width=20, textvariable=self.depatment)
        self.depatment_entry.grid(column=6, row=1)

        # Save button
        ttk.Button(addemp_sub_fr, text='Save', command=self.addNewEmp, style='back.TButton').grid(row=2, column=0, columnspan=3, sticky=(E,W))
        # Go back button
        ttk.Button(addemp_sub_fr, text='Go back', command=lambda: self.goBack(self.admin), style='back.TButton').grid(row=2, column=4, columnspan=3, sticky=(E,W))

        # Final touches
        for child in addemp_sub_fr.winfo_children():
            child.grid_configure(padx=10, pady=10)
        # Delete an employee sub frame window
        delemp_sub_fr = ttk.Frame(self.delemp_main_fr, padding=15, borderwidth=2, relief='sunken')
        delemp_sub_fr.grid(column=0, row=0)
        delemp_sub_fr.columnconfigure(0, weight=1)
        delemp_sub_fr.rowconfigure(0, weight=1)

        # Eid label text    
        ttk.Label(delemp_sub_fr, text="EId", style='myLabel.TLabel').grid(column=0, row=0)
        # Eid entry label
        self.user_given_eid = IntVar()
        self.user_given_eid_entry = ttk.Entry(delemp_sub_fr, width=20, textvariable=self.user_given_eid, font=('Times New Roman', 15))
        self.user_given_eid_entry.grid(row=0, column=1, sticky=(E,W))
        # Save button
        ttk.Button(delemp_sub_fr, text='Confirm', command=self.deleteEmp, style='back.TButton').grid(row=1, column=0, sticky=(E,W))
        # Go back button
        ttk.Button(delemp_sub_fr, text='Go back', command=lambda: self.goBack(self.admin), style='back.TButton').grid(row=1, column=1, sticky=(E,W))
        # Finla touches
        for child in delemp_sub_fr.winfo_children():
            child.grid_configure(padx=20, pady=20)
        # Update employee data sub frame widnow
        self.updateemp_sub_fr = ttk.Frame(self.updateemp_main_fr, padding=15, borderwidth=2, relief='sunken')
        self.updateemp_sub_fr.grid(column=0, row=0)
        self.updateemp_sub_fr.columnconfigure(0, weight=1)
        self.updateemp_sub_fr.rowconfigure(0, weight=1)

        ttk.Label(self.updateemp_sub_fr, text='Select Column', style='myLabel.TLabel').grid(row=0, column=0)
        select_col_fr = ttk.Frame(self.updateemp_sub_fr)
        select_col_fr.grid(row=0,column=1)
        # Inserting 7 column inside above frame
        ttk.Button(select_col_fr, text='EId', command=lambda: self.createInputFields('eId', IntVar(), IntVar(), 'Employee Eid', 'New Eid'), style='back.TButton').grid(row=0,column=0)
        ttk.Button(select_col_fr, text='Name', command=lambda: self.createInputFields('eName', IntVar(), StringVar(), 'Employee Eid', 'New Name'), style='back.TButton').grid(row=0,column=1)
        ttk.Button(select_col_fr, text='Gender', command=lambda: self.createInputFields('eGender', IntVar(), StringVar(), 'Employee Eid', 'New Gender'), style='back.TButton').grid(row=0,column=2)
        ttk.Button(select_col_fr, text='Age', command=lambda: self.createInputFields('eAge', IntVar(), IntVar(), 'Employee Eid', 'New Age'), style='back.TButton').grid(row=1,column=0)
        ttk.Button(select_col_fr, text='Salary', command=lambda: self.createInputFields('eSalary', IntVar(), IntVar(), 'Employee Eid', 'New Salary'), style='back.TButton').grid(row=1,column=1)
        ttk.Button(select_col_fr, text='Bonus', command=lambda: self.createInputFields('eBonus', IntVar(), IntVar(), 'Employee Eid', 'New Bonus'), style='back.TButton').grid(row=1,column=2)
        ttk.Button(select_col_fr, text='Department', command=lambda: self.createInputFields('eDepartment', IntVar(), StringVar(), 'Employee Eid', 'New Department'), style='back.TButton').grid(row=2,column=1)

        # Data entry frame
        self.input_fr = ttk.Frame(self.updateemp_sub_fr)
        self.input_fr.grid(row=1, column=0)

        # Variables
        self.input_filed_one = None
        self.input_filed_two = None
        self.whichColumn = None

        # Save button 
        ttk.Button(self.updateemp_sub_fr, text='Save', command=self.updateEmpDb, style='back.TButton').grid(row=2, column=0)
        # Back button
        ttk.Button(self.updateemp_sub_fr, text='Go Back', command=lambda: self.goBack(self.admin), style='back.TButton').grid(row=2, column=1)

        # Final Touches with padding
        for child in select_col_fr.winfo_children():
            child.grid_configure(padx=10, pady=10)
        for child in self.updateemp_sub_fr.winfo_children():
            child.grid_configure(padx=20, pady=20)
    
    def raiseLogInScreen(self):
        self.showFrame(self.mainframe)
    def logIn(self):
        self.mysql_name = str(self.name.get())
        self.mysql_password = str(self.password.get())
       
        # Connection mysql
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user=self.mysql_name,
                passwd=self.mysql_password,
                database="employee_database"
            )

            print('Connnection Successfull!!')
            self.cursor = self.connection.cursor()
            self.showFrame(self.admin)
            self.name_entry.delete(0, END)
            self.password_entry.delete(0, END)

        except Exception as e:
            print(e)
            self.name_entry.delete(0, END)
            self.password_entry.delete(0, END)
            messagebox.showerror('Log in fail', 'Possible causes :-\n1. Incorrect Name or Password\n2. Database missing\n3. No Inputs')

    def showFrame(self, frame):
        frame.tkraise()

    
    def goBack(self, frame):
        self.destroyInputFields()
        self.showFrame(frame)

    def raiseAdminWin(self):
        self.showFrame(self.admin)

    def raiseViewEmployeeWin(self):
        self.createDataLayout(self.data_content_fr)

        self.showFrame(self.employees_data_fr)

    def createDataLayout(self, parent_frame):
        # Fething employess data
        self.cursor.execute('SELECT * FROM employee')
        self.employees_data = self.cursor.fetchall()

        # Adding column heading
        ttk.Label(parent_frame, width=20, text='EId', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=0)
        ttk.Label(parent_frame, width=20, text='Name', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=1)
        ttk.Label(parent_frame, width=20, text='Gender', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=2)
        ttk.Label(parent_frame, width=20, text='Age', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=3)
        ttk.Label(parent_frame, width=20, text='Salary', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=4)
        ttk.Label(parent_frame, width=20, text='Bonus', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=5)
        ttk.Label(parent_frame, width=20, text='Department', borderwidth=1, relief=RIDGE, background='yellow').grid(row=0, column=6)

        i = 1
        for employee in self.employees_data:
            for j in range(len(employee)):
                e = ttk.Label(parent_frame, width=20, text=employee[j])
                e.grid(row=i, column=j)
            i += 1

    def destroyLayoutGoBack(self, previos_frame, current_frame):
        for widget in current_frame.winfo_children():
            widget.destroy()

        self.showFrame(previos_frame)
                
    def riaseAddempWin(self):
        self.showFrame(self.addemp_main_fr)

    def addNewEmp(self):
        new_employee_data = [self.eid, self.emp_name, self.gender, self.age, self.salary, self.bonus, self.depatment]

        try:
            insert_sql = "INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = []
            for data in new_employee_data:
                values.append(data.get())
            self.cursor.execute(insert_sql, values)
            self.connection.commit()
            messagebox.showinfo('Operation Successful', 'New Employee has been successfully added')
            self.goBack(self.admin)
        except exception as e:
            print(e)

        for entry in [self.eid_entry, self.emp_entry, self.gender_entry, self.age_entry, self.salary_entry, self.bonus_entry, self.depatment_entry]:
            entry.delete(0, END)

    def raiseDeleteEmpWin(self):
        self.showFrame(self.delemp_main_fr)

    def deleteEmp(self):
        eid = self.user_given_eid.get()
        print(eid, type(eid))
        try:
            delete_sql  = f"DELETE FROM employee WHERE eid = {eid}"
            self.cursor.execute(delete_sql)     
            self.connection.commit()
            messagebox.showinfo('Operation Successful', 'Employee has been successfully deleted')
            self.goBack(self.admin)
        except Exception as e:
            print(e)
            messagebox.showerror('Operation Failed', 'Please check EId again.')


        self.user_given_eid_entry.delete(0, END)

    def raiseUpdateEmpWin(self):
        self.showFrame(self.updateemp_main_fr)

    def createInputFields(self, column, field_one_type, filed_two_type, label1, label2):
        self.destroyInputFields()
        self.whichColumn = column
        self.input_filed_one = field_one_type
        self.input_filed_two = filed_two_type
        ttk.Label(self.input_fr, text=label1, style='myLabel.TLabel').grid(row=0, column=0)
        ttk.Entry(self.input_fr, textvariable=self.input_filed_one, width=20).grid(row=0, column=1)
        ttk.Label(self.input_fr, text=label2, style='myLabel.TLabel').grid(row=1, column=0)
        ttk.Entry(self.input_fr, textvariable=self.input_filed_two, width=20).grid(row=1, column=1)

        # Final Touches
        for child in self.input_fr.winfo_children():
            child.grid_configure(padx=10, pady=10)

    def updateEmpDb(self):
        try:
            update_sql = f"UPDATE employee SET {self.whichColumn} = '{self.input_filed_two.get()}' WHERE eId = {self.input_filed_one.get()}"
            self.cursor.execute(update_sql)

            self.connection.commit()
            messagebox.showinfo('Operation Successful', 'Employee data has been successfully upated')
            # Delte those input fields
            self.destroyInputFields()
            self.goBack(self.admin)
            
        except Exception as e:
            print(e)

    def destroyInputFields(self):
        for widget in self.input_fr.winfo_children():
            widget.destroy()
        
    def drawTotalSalaryGraph(self):
        total_salary_by_department = self.fetchTotalSalaryDept()
        df = self.createDataFrame(total_salary_by_department, "Total Salary", "Departments")
        
        plt.bar(df['Departments'], df['Total Salary'], width = 0.4)
        plt.xlabel('Departments')
        plt.ylabel('Total Salary')
        plt.title('Total Salary given in Differnet Departments')
        plt.show()
    
    def drawTotalBonusGraph(self):
        total_bonus_by_department = self.fetchTotalBonusDept()
        df = self.createDataFrame(total_bonus_by_department, "Total Bonus", "Departments")

        plt.bar(df['Departments'], df['Total Bonus'], width=0.4)
        plt.xlabel('Departments')
        plt.ylabel('Total Bonus')
        plt.title('Total Bonus given in Differnet Departments')
        plt.show()

    def drawAvgSalaryGraph(self):
        avg_salary_by_department = self.fetchAvgSalaryDept()
        df = self.createDataFrame(avg_salary_by_department, "Average Salary", "Departments")

        plt.bar(df['Departments'], df['Average Salary'], width=0.4)
        plt.xlabel('Departments')
        plt.ylabel('Average Salary')
        plt.title('Average Salary given in Differnet Departments')
        plt.show()

    def drawAvgBonusGraph(self):
        avg_bonus_by_department = self.fetchAvgBonusDept()
        df = self.createDataFrame(avg_bonus_by_department, "Average Bonus", "Departments")

        plt.bar(df['Departments'], df['Average Bonus'], width=0.4)
        plt.xlabel('Departments')
        plt.ylabel('Average Bonus')
        plt.title('Average Bonus given in Differnet Departments')
        plt.show()

    def fetchTotalSalaryDept(self):
        self.cursor.execute('SELECT SUM(eSalary), eDepartment FROM employee GROUP BY eDepartment')
        return self.cursor.fetchall()

    def fetchTotalBonusDept(self):
        self.cursor.execute('SELECT SUM(eBonus), eDepartment FROM employee GROUP BY eDepartment')   
        return self.cursor.fetchall()

    def fetchAvgSalaryDept(self):
        self.cursor.execute('SELECT AVG(eSalary), eDepartment FROM employee GROUP BY eDepartment')   
        return self.cursor.fetchall()
    
    def fetchAvgBonusDept(self):
        self.cursor.execute('SELECT AVG(eBonus), eDepartment FROM employee GROUP BY eDepartment')   
        return self.cursor.fetchall()

    def createDataFrame(self, data, *column_names):
        return pd.DataFrame(data, columns=column_names)
root = Tk()
app = EmployeeManagement(root)
# Starting mainloop
root.mainloop()