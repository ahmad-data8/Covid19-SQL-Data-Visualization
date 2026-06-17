import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

print("==================================================")
print("        SQL & DATA VISUALIZATION PROJECT          ")
print("==================================================")

# 1. Create a local SQL Database in memory and dump data into it
conn = sqlite3.connect(':memory:')  # Creating a temporary SQL database
cursor = conn.cursor()

# Create Table using SQL
cursor.execute('''
    CREATE TABLE covid_data (
        Country TEXT,
        Total_Cases INTEGER,
        Total_Deaths INTEGER,
        Recovery_Rate REAL
    )
''')

# Insert Data using SQL
raw_data = [
    ('USA', 1000000, 20000, 95.5),
    ('India', 850000, 15000, 97.2),
    ('Brazil', 600000, 18000, 92.1),
    ('Pakistan', 150000, 3000, 96.8),
    ('Germany', 400000, 5000, 98.0)
]
cursor.executemany('INSERT INTO covid_data VALUES (?, ?, ?, ?)', raw_data)
conn.commit()
print("Success: SQL Database created and data inserted successfully!")

# 2. Run an SQL Query to fetch countries with Recovery Rate > 95%
print("\n--- Running SQL Query: Countries with Recovery Rate > 95% ---")
sql_query = "SELECT Country, Recovery_Rate FROM covid_data WHERE Recovery_Rate > 95.0 ORDER BY Recovery_Rate DESC"
df_sql = pd.read_sql_query(sql_query, conn)
print(df_sql.to_string(index=False))

# 3. Data Visualization (Creating a Bar Chart of Total Cases)
print("\nGenerating Bar Chart for Total Cases...")
df_all = pd.read_sql_query("SELECT Country, Total_Cases FROM covid_data", conn)

# Plotting the graph
plt.figure(figsize=(8, 5))
plt.bar(df_all['Country'], df_all['Total_Cases'], color=['blue', 'orange', 'green', 'red', 'purple'])
plt.title('Global Covid-19 Total Cases by Country')
plt.xlabel('Country')
plt.ylabel('Number of Cases (in Millions)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display the graph window
print("Close the graph window to finish the script.")
plt.show()

# Close SQL Connection
conn.close()