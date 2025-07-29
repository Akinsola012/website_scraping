import streamlit as st
import sqlite3
import pandas as pd

# Page config
st.set_page_config(page_title="Indeed Job Insights", layout="wide")
st.title("Indeed Job Market Dashboard")

# Connect to the database
conn = sqlite3.connect("indeed_jobs.db")

# Raw Data
df = pd.read_sql("SELECT * FROM jobs", conn)

# Overview Metrics
st.subheader("Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Jobs", len(df))
col2.metric("Unique Companies", df['company'].nunique())
col3.metric("Remote-Friendly %", round((df['remote_or_onsite'].str.lower().str.contains("remote").sum() / len(df)) * 100, 2))

st.divider()

# Interactive Filters
st.sidebar.header("Filters")
locations = st.sidebar.multiselect("Filter by Location", options=sorted(df['location'].unique()))
job_types = st.sidebar.multiselect("Filter by Job Type", options=sorted(df['job_type'].unique()))

filtered_df = df.copy()
if locations:
    filtered_df = filtered_df[filtered_df['location'].isin(locations)]
if job_types:
    filtered_df = filtered_df[filtered_df['job_type'].isin(job_types)]

# Top Job Titles
st.subheader("Top Job Titles")
title_data = (
    filtered_df.groupby("title")
    .size()
    .reset_index(name="openings")
    .sort_values(by="openings", ascending=False)
    .head(15)
)
st.bar_chart(title_data.set_index("title"))

# Top Companies
st.subheader("Companies Hiring Most")
company_data = (
    filtered_df.groupby("company")
    .size()
    .reset_index(name="postings")
    .sort_values(by="postings", ascending=False)
    .head(15)
)
st.bar_chart(company_data.set_index("company"))

# Remote vs Onsite
st.subheader("Remote vs Onsite")
remote_data = (
    filtered_df.groupby("remote_or_onsite")
    .size()
    .reset_index(name="count")
)
st.dataframe(remote_data, use_container_width=True)

# Job Type Distribution
st.subheader("Job Types")
job_type_data = (
    filtered_df.groupby("job_type")
    .size()
    .reset_index(name="count")
)
st.dataframe(job_type_data, use_container_width=True)

# View Jobs Table
with st.expander("View Full Job Listings"):
    for i, row in filtered_df.iterrows():
        st.markdown(f"**{row['title']}** at *{row['company']}* — {row['location']} ({row['job_type']})")
        st.markdown(f"[Apply Here]({row['link']})", unsafe_allow_html=True)
        st.text("---")

conn.close()