import json
import psycopg2

# Replace these with your PostgreSQL connection details
dbname = "your_database_name"
user = "your_username"
password = "your_password"
host = "your_host"
port = "your_port"

# JSON file path
json_file_path = "your_data.json"

# Open and read the JSON file
with open(json_file_path, "r") as file:
    data = json.load(file)

# Establish a connection to the PostgreSQL database
connection = psycopg2.connect(
    dbname=dbname, user=user, password=password, host=host, port=port
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Iterate through the data and insert it into the PostgreSQL table
for row in data:
    columns = ", ".join(row.keys())
    values = ", ".join(["%s" for _ in row.values()])
    insert_query = f"INSERT INTO your_table_name ({columns}) VALUES ({values});"
    cursor.execute(insert_query, tuple(row.values()))

# Commit the changes and close the connection
connection.commit()
connection.close()
