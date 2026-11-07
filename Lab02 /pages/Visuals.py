# This creates the page for displaying data visualizations.

import streamlit as st
import json
import pandas as pd
import altair as alt
import plotly.express as px

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("Data Visualizations 📈 Soccer!")


# PART 1: GRAPHS FROM data.json
# --- YOUR CODE GOES HERE ---

with open("data.json") as f:
    data = json.load(f)
    
df=pd.DataFrame(data["data_points"])


#1 scatter static 
st.subheader("Goals vs. Assists Scatter Plot")


chart = (
    alt.Chart(df)                      # which DataFrame?
    .mark_circle(size=100)                # dots instead of bars or lines
    .encode(
        x=alt.X("Goals", title="Goals"),      # which column, and what the axis label says
        y=alt.Y("Assists", title="Assists"),
        tooltip=["Player", "Goals", "Assists"],    # columns to show on hover
    )
    .properties(title="Ballon d'Or 2026 Contenders: Club Stats, 2025-26")              # chart title
)

st.altair_chart(chart, use_container_width=True)

#2 Dynamic Bar Chart

if "selected_stat" not in st.session_state:
    st.session_state["selected_stat"] = "Goals"

st.subheader("Bar graph of chosen statistic")

selected_stat = st.radio(
    "What stat of the players do you want to see?",
    ["Goals", "Assists", "Dribbles per Game"],
    key="selected_stat",
)



st.bar_chart(df, x="Player", y=selected_stat, color="Player")

# PART 2: GRAPHS FROM data.csv
surveyInfo=pd.read_csv("data.csv")

#PIE CHART:
st.subheader("Pie Chart Percentages!")
Votes=surveyInfo["Player"].value_counts().reset_index()
Votes.columns = ["Player", "Votes"]

Chart= px.pie(Votes, names="Player", values="Votes", title="Who Should Have Won the Ballon d'Or 2026? Based on The SurveyVotes")
st.plotly_chart(Chart, use_container_width=True)

#BAR GRAPH
league_votes = surveyInfo["Hardest League"].value_counts().reset_index()
league_votes.columns = ["Most Competitive League", "Votes"]

st.subheader("Bar graph of Choices for Question of most competitive leagues ")
st.bar_chart(league_votes, x="Most Competitive League", y="Votes")
st.caption("Some varied opinions. Fill out the sruvey for your vote to be reflected in the chart.")

#Dynamic\

# DYNAMIC CHART
mean = surveyInfo.groupby("Player")["Hours Per Week"].mean().reset_index()
median= surveyInfo.groupby("Player")["Hours Per Week"].median().reset_index()

if "selected_summary" not in st.session_state:
    st.session_state["selected_summary"] = "Mean"

st.subheader("A bar chart for you to identify relation between watched time vs player they chose to win Ballon D'or")

summaryChoice = st.radio("Which summary you want to see?",["Mean", "Median"],key="selected_summary")

if summaryChoice == "Mean":
    shown = mean
else:
    shown =median

st.bar_chart(shown, x="Player", y="Hours Per Week", color="Player")
st.caption("Do you find a relation between the hours watched with the soccer slected? Is there a trend that maybe people that do not watch soccer are being influenced by media. We can see the people that sleected Messi, have less amount of avarage time")

