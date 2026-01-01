# Here we are going to know about some database related operations in python using the inbuilt function SQLITE3

''' SQL(Structured Query Language) is a structured language for managing as well as manipulating relational databases.Sqlite is a self contained, serverless and zero-configuration database engine which is widely used for embedded database systems.'''
# Here first we have to import the sqlite3
import sqlite3
# Then we need to establish the connection between the database so we have
connection = sqlite3.connect('Employee.db')
# Now we are going to create the cusor object to interact with the employee database
cursor = connection.cursor()
# Now we hare going to create a table inside the employee database.
cursor.execute('''drop table if exists Employee''')
cursor.execute(
    '''Create table if not exists Employee(
        sapid integer primary key,                                    
        name text not null,
        company text not null,
        jobrole text not null,
        tech_stack text
    )'''
)
# Now we are going to commit the changes so we have
connection.commit()
print(f'The table has been successfully created')
print()
# Now we are going to insert some value in the table so we have
cursor.execute('''insert into Employee(sapid,name,company,jobrole,tech_stack) values(2345,'Jhon Deo','Oracle','SDE','Backend')''')
cursor.execute('''insert into Employee(sapid,name,company,jobrole,tech_stack) values(2377,'Mark','Microsoft','SDE','Frontend')''')
cursor.execute('''insert into Employee(sapid,name,company,jobrole,tech_stack) values(2380,'Jack Buzz','Google','Software Engineer','QA-Automation')''')
cursor.execute('''insert into Employee(sapid,name,company,jobrole,tech_stack) values(2386,'Peter','Amazon','Data Scientist','Backend')''')
print(f'The record has been successfully created')
# No we are going to commit the changes so we have
connection.commit()
print()
# Now we are going to fetch all the data from the table then we have
cursor.execute('''select * from Employee''')
rows = cursor.fetchall()
print(f'The all records are:')
for row in rows:
    print(row)
# Here there is a requirement that for a particular person the job role got change so we have
cursor.execute('''update Employee set tech_stack = 'Machine Learning' where sapid = 2386''')
connection.commit()
print(f'The record has been updated')
print()
cursor.execute('''select * from Employee''')
print(f'The updated record becomes:')
for row in cursor.fetchall():
    print(row)
print()
# Here the situation happend in a such a way that the person having sapId 2286 has beed resigned the company so we have
cursor.execute('''delete from Employee where sapid = 2386''')
connection.commit()
print(f'The record has been successfully updated')
cursor.execute('''select * from Employee''')
rows = cursor.fetchall()
for row in rows:
    print(row)
# Now all the procedure done hence closeing the session
connection.close()
