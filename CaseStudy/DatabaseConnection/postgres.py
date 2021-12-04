from sys import _clear_type_cache
import psycopg2
import os

# Connect to the database the hostname = localhost, username = 'postgres, password = 'Green448800$, and database = 'postgres' port = 5432
database = 'postgres'
user = 'postgres'
password = 'Green448800$'
host = 'localhost'
port = '5432'

path = './Data/document.csv'
# check if the file exists
if os.path.exists(path):
    print('File exists')
else:
    print('File does not exist')

try:
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)

    cur = conn.cursor()
    print("Connected to the database")
    # create table named All_movies_data and id movie_id, list_of_all_movies
    cur.execute("CREATE TABLE IF NOT EXISTS All_movies_data (movie_id serial PRIMARY KEY, list_of_all_movies varchar(100))")
    All_movies_data = open(path, 'r')
    arr = []
    for d in All_movies_data:
        # remove the commas surrounding the d
        d = d.replace('"', '')
        for i in d.split(','):
            # insert i into the all_movies_data table
            cur.execute("INSERT INTO All_movies_data (list_of_all_movies) VALUES (%s)", (i,))
    # check if the data of the table is contains values of non letters
    cur.execute("SELECT * FROM All_movies_data")
    for row in cur:
        print(row)
    conn.commit()
    conn.close()
    
except:
    print("Unable to connect to the database")


    
  

    

