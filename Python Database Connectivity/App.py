# Here we are going to create the streamlit based application such that it will recieve the data from the user and display the information in the tabular form. 

from Employee import Employee
import streamlit as st 
import sqlite3
import pandas as pd

# Now we are going to establish the connection with the database so we have
connection = sqlite3.connect('Storage.db')
# Now we are going to to declare the cursor object to interact with the database so we have
cursor = connection.cursor()

# Now we are going to create a form using streamlit
st.title('Employee Details')
with st.form('Employee_Data',clear_on_submit=True):
    employee_id = st.text_input('Enter the employee id:')
    name = st.text_input('Enter the name:')
    age = st.text_input('Enter the age:')
    department = st.text_input('Enter the department:')
    designation = st.text_input('Enter the designation:')
    salary = st.text_input('Enter the salary:')
    email = st.text_input('Enter the email id:')
    phone = st.text_input('Enter the phone number:')
    date_of_joining = st.text_input('Enter the date of joining:')
    submit = st.form_submit_button(label='Register')
    
# Now we are going to save the information stored in the employee object into the database, so we have

cursor.execute('''
    create table if not exists Employee(
        employee_id integer not null unique,
        name text not null,
        age integer not null,
        department text not null,
        designation text not null,
        salary integer not null,
        email text not null unique,
        phone text not null,
        date_of_joining date not null
    )
''')
connection.commit()
# Now we are going to commit the changes so we have
connection.commit()
# Now we are going to save the form data into the database so we have

def save_data(emp:Employee):
    cursor.execute('''insert into Employee(employee_id,name,age,department,designation,salary,email,phone,date_of_joining)
                   values(?,?,?,?,?,?,?,?,?)''',(emp.employee_id,emp.name,emp.age,emp.department,emp.designation,emp.salary,emp.email,emp.phone,emp.date_of_joining))
    connection.commit()
# Now we are going to devlope the condition such that if the user clicks the submit button then then entered form data will save in the form of object of the employee class, so we have
if __name__ == '__main__':
    
    if submit:
        employee = Employee(employee_id,name,age,department,designation,salary,email,phone,date_of_joining)
        save_data(employee)
        st.success(f'The form data has been saved successfully')
    # Now we are going to devlope an ETL pipeline such that it will extract the form data and perform some operations on them and load into the streamlit dashboard.
    def Extract():
        cursor.execute('select * from Employee')
        return cursor.fetchall()
    def Transform(data):
        columns = ['Employee id','Name','Age','Department','Designation','Salary','Email','Contact Info','Date Of Joining']
        employee_df = pd.DataFrame(data,columns=columns)
        employee_df["Email"] = employee_df["Email"].str.strip().str.lower()
        employee_df["Name"]  = employee_df["Name"].str.strip()
        # Now we are going to remove duplicate entries
        employee_df = employee_df.drop_duplicates(subset = ['Employee id','Email'],keep='first')
        return employee_df
    def load(employee_df):
        employee_df.to_csv('Employee_data.csv',index=False)
    data = Extract()
    employee_df = Transform(data)
    load(employee_df)
    # Now we are going to display the form data in streamlit as an interactive dashboard so we have
    if st.button('View Details'):
        df = pd.read_csv('Employee_data.csv')
        st.success('Employee records has been loaded successfully')
        st.dataframe(df)
    # Now we are going to close the connection
    connection.close()

    

    
    






    