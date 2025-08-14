# Here we are going to create a simpleapplication in python using streamlit web framework.
# Now we are going to import the particular libraries so for that we have
import numpy as np
import pandas as pd
import streamlit as st 
# Now we are going to define the title of the application to be buid so we have
st.title('Hello Streamlit')
# Now we are going to display a simple text in the web app so we have
st.write("This is a simple text")
# Now we are going to create a dataframe and display over the web app so we have
d = {
    'Name':['Subhasish','Muskan','Nibedita','Subham','Piyush'],
    'marks':[76,94,87,84,85]
}
df = pd.DataFrame(d)
st.write('Here is the dataframe')
st.write(df)
# Now we are going to create a simple line chart
chart_data = pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(chart_data)
# Now we are going to define a simple text field such that it asks a name of a person as input from the user and if once it gets the correct string format it will display in the window.
st.title('Streamlit text window')
name = st.text_input('Enter your name:')
if name:
    st.write(f"Hello, {name}")
# Now we are going to create the age slider such that as the slider of the pointer goes increasing the particulaar age should be display in the screen
age = st.slider("Select your age:",0,100,25)
st.write(f"your age is {age}")
# Now we are going to create a selectbox where user can choose the particular language to learn, once after selecting it got displayed in the screen
options = ['Python','C++','Java','JavaScript']
choice = st.selectbox('Choose your favourite language:',options)
st.write(f'you selected {choice}.')
# Now we are going to write a program such that it asks user to upload a particular file from the local and display the content
# Here we are going to create a function for that
st.title("File Upload Example")
def upload(uploaded_file):
    if uploaded_file is not None:  # ✅ Check before accessing .name
        st.success(f"Uploaded file: {uploaded_file.name}")
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
            st.write("### CSV File Preview")
            st.dataframe(df)
        elif uploaded_file.name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file)
            st.write("### Excel File Preview")
            st.dataframe(df)
        elif uploaded_file.name.endswith(".txt"):
            content = uploaded_file.read().decode("utf-8")
            st.text(content)
    else:
        st.warning("Please upload a file to proceed.")
uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt", "xlsx"])
upload(uploaded_file)
 