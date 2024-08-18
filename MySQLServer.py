import mysql.connector

# Database connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass"
)

mycursor = mydb.cursor()

# Create the database (ignore error if it already exists)
try:
    sql = "CREATE DATABASE alx_book_store"
    mycursor.execute(sql)
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as err:
    print("Database creation failed:", err)
    # Ignore error if it already exists
    #if err.errno == mysql.connector.Error.er.db_exists_err:
      #print("Database 'alx_book_store' already exists. Continuing...")
# Close the connection
mydb.close()