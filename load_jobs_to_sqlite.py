import pandas as pd
import sqlite3

# Read the CSV
df = pd.read_csv('USA_python_jobs.csv')

# Connect to (or create) SQLite DB
conn = sqlite3.connect('indeed_jobs.db')

# Push the DataFrame into a table
df.to_sql('jobs', conn, if_exists='replace', index=False)

conn.close()