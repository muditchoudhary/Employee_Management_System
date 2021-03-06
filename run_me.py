from logging import exception
import mysql.connector
from mysql.connector import connection
# global variables
mysql_name = None
mysql_password = None

def createEmployeeDb():
    global mysql_name, mysql_password
    try:
        mysql_name = input("Enter your mysql name : ")
        mysql_password = input("Enter your mysql password : ")
        connecion = mysql.connector.connect(
                        host="localhost",
                        user=mysql_name,
                        passwd=mysql_password
                    )
    except exception as e:
        print(e)

    cursor = connecion.cursor()
    cursor.execute("CREATE DATABASE employee_database")

    connecion.close()

def createEmployeeTable():
    try:
        connecion = mysql.connector.connect(
            host="localhost",
            user=mysql_name,
            passwd=mysql_password,
            database='employee_database'
        )

    except exception as e:
        print(e)

    cursor = connecion.cursor()

    tableName ="""CREATE TABLE employee
                (
                    eId int PRIMARY KEY,
                    eName VARCHAR(50),
                    eGender VARCHAR(8),
                    eAge int,
                    eSalary int,
                    eBonus int,
                    eDepartment VARCHAR(25)
                );"""

    cursor.execute(tableName)

    sql = "INSERT INTO employee (eId, eName, eGender, eAge, eSalary, eBonus, eDepartment) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = [
        (501, 'Aman Singh', 'Male', 23, 15000, 2000, 'Customer Care'),
        (502,'Rajeev Jain', 'Male', 45, 60000, 0, 'Production'),
        (503, 'Gautam Motwani',	'Male',	26,	15000, 2000, 'Customer Care'),
        (504, 'Kripesh Agarwa',	'Male', 30, 15000, 2000, 'Customer Care'),
        (505, 'Shanti Sharma', 'Female', 35, 25000, 3500, 'HR'),
        (506, 'Neha Rathore', 'Female', 21,	15000, 2000, 'Customer Care'),
        (507, 'Gaurav Jain', 'Male', 25, 15000, 2000, 'Customer Care'),
        (508, 'Amit Berwa', 'Male',	30, 25000, 3500, 'HR'),
        (509, 'Ayushi Dass', 'Female', 29, 15000, 2000, 'Customer Care'),
        (510, 'Sumit Devnath', 'Male', 38, 35000, 5000, 'Sales'),
        (511, 'Diya Gupta', 'Female', 22, 15000, 2000, 'Customer Care'),
        (512, 'Nidhi Jangid', 'Female', 45,	60000, 0, 'Production'),
        (513, 'Krishna Kumawat', 'Female', 35, 35000, 5000, 'Sales'),
        (514, 'Aryan Khan', 'Male',	27,	15000, 2000, 'Customer Care'),
        (515, 'Riya Shekhawat', 'Female', 22, 15000, 2000, 'Customer Care'),
        (516, 'Narendra Kumar Choudhary', 'Male', 26, 15000, 2000, 'Customer Care'),
        (517, 'Aditya Bajaj', 'Male', 23, 15000, 2000, 'Customer Care'),
        (518, 'Nitin Kumar', 'Male', 28, 15000, 2000, 'Customer Care'),
        (519, 'Naman Mathur', 'Male', 30, 35000, 5000, 'Sales'),
        (520, 'Tanmay Singh', 'Male', 35, 35000, 5000, 'Sales'),
        (521, 'Mukul Roy', 'Male', 39, 35000, 5000, 'Sales'),
        (522, 'Mishti Gupta', 'Female',	21, 15000, 2000, 'Customer Care'),
        (523, 'Yashika Gurjar', 'Female', 30, 25000, 3500, 'HR'),
        (524, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),        
        (525, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (526, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (527, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (528, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (529, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (530, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (532, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (533, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (534, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (535, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (536, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (537, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (538, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (539, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (540, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (541, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (542, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (543, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (544, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (545, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (546, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care'),
        (547, 'Hari Singh Sehkhawat', 'Male', 22, 15000, 2000, 'Customer Care')
    ]

    cursor.executemany(sql, val)
    
    connecion.commit()
    connecion.close()

createEmployeeDb()
createEmployeeTable()