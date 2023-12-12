import json
import psycopg2

# Replace these with your PostgreSQL connection details
dbname = "optimum-pc-build-db"
user = "postgres"
password = "Passw0rd!"
host = "localhost"
port = "5432"

# JSON file path
json_file_path = "C:\\Users\\kishore sathe\\Desktop\\Workspace\\DB data optimum-pc-builds\\speaker.json"

# Open and read the JSON file
with open(json_file_path, encoding="utf8") as file:
    data = json.load(file)

# Establish a connection to the PostgreSQL database
connection = psycopg2.connect(
    dbname=dbname, user=user, password=password, host=host, port=port
)

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

print(cursor.execute(f"select * from public.speaker"))
# Iterate through the data and insert it into the PostgreSQL table
for row in data:
    columns = ", ".join(row.keys())
    values = ", ".join(["%s" for _ in row.values()])
    insert_query = f"INSERT INTO public.speaker ({columns}) VALUES ({values});"
    cursor.execute(insert_query, tuple(row.values()))

# Commit the changes and close the connection/
print(cursor.execute(f"select * from public.speaker"))

connection.commit()
connection.close()
    