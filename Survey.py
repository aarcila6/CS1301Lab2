# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Survey",
    page_icon="📝",
)

# PAGE TITLE AND USER DIRECTIONS
st.title("Data Collection Survey 📝")
st.write("Please fill out the form below to add your data to the dataset.")

# DATA INPUT FORM
# 'st.form' creates a container that groups input widgets.
# The form is submitted only when the user clicks the 'st.form_submit_button'.
# This is useful for preventing the app from re-running every time a widget is changed.
with st.form("survey_form"):
    # Create text input widgets for the user to enter data.
    # The first argument is the label that appears above the input box.
    player = st.selectbox("Who do you think deserved...” the Ballon D'or(If you don't choose will be Kane and La Liga as Default)",["Kane", "Mbappe", "Yamal", "Olise", "Haaland", "Dembele", "Messi", "Kvaratskhelia"] )
    league = st.selectbox("What league do you think is the most competitive?", ["La Liga(Spain)","Ligue 1(France)","Bundesliga(Germany)", "Premier League(England)", "MLS(USA)", "Serie A(Italy)" ])
    hours = st.text_input("How many hours per week in average do you think you watch soccer")
    try:
        hours = float(hours)
        valid = True
    except ValueError:
        valid = False
    

    # The submit button for the form.
    submitted = st.form_submit_button("Submit Data")

    # This block of code runs ONLY when the submit button is clicked.
    if submitted:
        if valid:
            # 2. build the line
            DataLine = player + "," + league + "," + str(hours) + "\n"
    
            with open("data.csv", "a") as f:
                f.write(DataLine)
            st.success("Your choices have been recorded. Thank you for filling the survey out!")
            st.write(f"You entered: **Your Winner Player:** {player}")
            st.write(f"You entered: **Most Competitive league:** {league}")
            st.write(f"You entered: **Hours per week you watch soccer:** {hours}")

        else:
            st.error("Your have inserted an invalid input into de 3rd question, plese enter something like 5, or 7.5")                 


# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
st.header("Current Data in CSV")

# Check if the CSV file exists and is not empty before trying to read it.
if os.path.exists('data.csv') and os.path.getsize('data.csv') > 0:
    # Read the CSV file into a pandas DataFrame.
    current_data_df = pd.read_csv('data.csv')
    # Display the DataFrame as a table.
    st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")
